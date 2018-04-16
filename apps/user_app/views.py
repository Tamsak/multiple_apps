from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "user_app/index.html")
def login(request):
    return render(request, "user_app/login.html")
def new_user(request):
    return redirect("/register")
def users(request):
    return render(request, "user_app/users.html")
