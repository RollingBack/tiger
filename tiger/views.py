#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 上午10:40
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : views.py
# @Software: PyCharm

from django.shortcuts import render


def home(request):
    return render(request, 'tiger/index.html')


def sign_in(request):
    return render(request, 'tiger/login.html')


def console(request):
    return render(request, 'tiger/console.html')