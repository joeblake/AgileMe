from django.shortcuts import render, redirect

def redirect_home(request):
    response = redirect('/boards/')
    return response
