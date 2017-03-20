#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 上午10:40
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : views.py
# @Software: PyCharm

from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required


@login_required(login_url='/sign-in')
def home(request):
    return render(request, 'tiger/index.html')


def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('user_name', '')
            password  = request.POST.get('password', '')
            user = authenticate(username=user_name, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if request.POST.get('next') != '':
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect('/')
        return render(request, 'tiger/login.html', {'wrong_password': True})
    return render(request, 'tiger/login.html')


@login_required(login_url='/sign-in')
def console(request):
    return render(request, 'tiger/console.html')


@login_required(login_url='/sign-in')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/sign-in')