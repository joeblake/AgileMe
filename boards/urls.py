from django.urls import path
from django.views.generic import TemplateView
from django.contrib import auth

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('do_work/', views.do_work_view, name = 'work_view'),
    path('new_board/', views.new_board_view, name = 'new_board_view'),
    path('login/', auth_views.LoginView.as_view(template_name="boards/login.html", extra_context = {'user_creation_form' : UserCreationForm()})),
    path('logout/',views.logout_view, name = 'logout'),
    path('board_delete/', views.board_delete_view, name = 'board_delete_view'),
    path('scrum/', views.scrum_view, name = 'scrum_view'),
    path('scrum/submit/', views.scrum_submit_view, name ="scrum_submit_view"),
    path('login/process/', auth_views.LoginView.as_view(template_name = "boards/login.html",extra_context = {'user_creation_form' : UserCreationForm()})),
    path('login/createuser/', views.process_create_user, name = "process_create_user"),
    path('process_task', views.process_task),
]
