# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, "DojoApp/index.html")
def new(request):
    return render(request, "DojoApp/new.html")
def create(request):
    return redirect('/index.html')
def show(request,blog):
    response = "Display Blog: %s" % blog
    return HttpResponse(response)
def edit(request, blog):
    response = "Place holder to edit blog: %s" % blog
    return HttpResponse(response)
def destroy(request,blog):
    return redirect('/')