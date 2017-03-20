#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 下午2:20
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : forms.py
# @Software: PyCharm
from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(label='user_name', max_length=100)
    password = forms.CharField(label='password', max_length=100)

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            super(LoginForm, self).clean()