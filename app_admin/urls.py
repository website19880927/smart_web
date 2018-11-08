#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ricardo
@license: (C) Copyright 2018-2019 @yang.com Corporation Limited.
@contact: 659706575@qq.com
@software: made@Yang
@file: urls.py
@time: 2018/11/8 0008 13:30
@desc:
'''
from django.urls import path, include

from app_admin import views

urlpatterns = [
    path('page/',include([
        path('login/',views.login_port,name='login'),
        path('logic/',views.login_logic,name='logic'),

    ])),
    path('phone/', views.phone, name='phone'),
]



