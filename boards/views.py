from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics
from .models import Board, Task
from django.template import loader
from .forms import TaskForm, WorkForm, BoardForm, BoardDelete, ScrumForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

@login_required
def scrum_submit_view(request):
    if(request.method == 'POST'):
        form = ScrumForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            tasks = data["task_ids"][:-1].split(",")
            print("---")
            print(tasks)
            print("---")
            scrum_tasks = [Task.objects.get(id = int(x)) for x in tasks]
            print(scrum_tasks)
            for t in list(Task.objects.filter(board__user = request.user)):
                if t  in scrum_tasks:
                    t.in_scrum = True
                else:
                    t.in_scrum = False
                t.save()
        else:
            print(form.errors)
    return redirect('/boards/')

def board_delete_view(request):
    if(request.method == 'POST'):
        form = BoardDelete(request.POST)

        if(form.is_valid()):
            data = form.cleaned_data
            b = Board.objects.get(pk = data['board_id'])
            b.delete()
    return redirect('/boards/')

def login_or_createuser_view(request):
    context = {
        "login_form" : AuthenticationForm(),
        "user_creation_form" : UserCreationForm(),
    }
    return render(request, 'boards/login.html',context)

def process_login(request):
    print('processing login')
    if request.method == 'POST':
        print('method is post')
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            print('user logged in')
        else:
            print('user not found')
            print(request.POST)
            login_form = AuthenticationForm(request.POST)
            print(login_form.is_valid())
            print(login_form.is_bound)
            print(login_form.errors.as_data())
            context = {
            'errors' : login_form.errors,
            'login_form' : login_form,
            'user_creation_form' : UserCreationForm(),
            }
            return render(request,'boards/login.html', context)
    else:
        print('method not post')
    return redirect('/boards/')

def process_create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created succesfully')
        else:
            print('creation invalid')
            context = {
            'user_creation_form' : form ,
            'form' : AuthenticationForm(),
            }
            return render(request, 'boards/login.html' , context)
    return redirect('/boards/')

def logout_view(request):
    logout(request)
    return(redirect('/boards/login'))

def new_board_view(request):
    if(request.method == 'POST'):
        form = BoardForm(request.POST)

        if(form.is_valid()):
            data = form.cleaned_data
            b = Board(name = data['name'], user = User.objects.get(pk = data['user_id']), use_due_date = data['use_due_date'])
            b.save()
        else:
            print(form.errors)
        response = redirect('/boards/')
        return response

def do_work_view(request):
    if(request.method == 'POST'):
        form = WorkForm(request.POST)

        #Check if form is valid
        if(form.is_valid()):
            data = form.cleaned_data
            task = Task.objects.get(pk = data['task_id'])
            task.do_work(data['points'])
        else:
            print(form.errors)
        response = redirect('/boards/')
        return response

@login_required
def scrum_view(request):

    # Get the user, generate a board map just like index view.
    user = request.user
    board_list = list(Board.objects.filter(user = user))
    boardmap = {}
    for board in board_list:
        boardmap[board] = list(Task.objects.filter(board = board))

    tasklist = []
    for tl in boardmap.values():
        tasklist.extend(tl)
    taskstring = ""
    for t in tasklist:
        taskstring = taskstring + str(t.id) + ","

    context = {
    'board_map' : boardmap,
    'task_string' : taskstring,
    'user' : user,
    'scrum_form' : ScrumForm(),
    }
    return render(request,'boards/scrum.html' , context)

def process_task(request):
    # Check if we are processing a form return
    if(request.method == 'POST'):
        form = TaskForm(request.POST)

        #Check if form is valid
        if(form.is_valid()):
            data = form.cleaned_data
            #Create the new task from the data in the form
            board = Board.objects.get(pk = data['board_id'])
            if(board.use_due_date):
                t = Task(board = board, name = data['name'], points = data['points'], due_date = data['date'])
            else:
                t = Task(board= board, name = data['name'], points = data['points'])
            print(t)
            t.save()
        else:
            print(form.errors)
        #redirect back to page
        return redirect('/boards/')


@login_required
def index(request):
    #get the current user
    user = request.user

    #get list of user's boards
    board_list = list(Board.objects.filter(user = user))
    boardmap = {}

    # Map each board to a list of its tasks
    for board in board_list:
        boardmap[board] = list(Task.objects.filter(board = board))

    scrum_tasks = list(Task.objects.filter(board__user = user).filter(in_scrum = True))

    template = loader.get_template('boards/index.html')
    context = {
        'board_form' : BoardForm(),
        'work_form' : WorkForm(),
        'task_form' : TaskForm(),
        'scrum_tasks' : scrum_tasks,
        'user'  : user,
        'board_list' : board_list,
        'board_map' : boardmap,
        }
    return render(request,'boards/index.html',context)
