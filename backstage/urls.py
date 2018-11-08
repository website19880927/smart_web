#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ricardo
@license: (C) Copyright 2018-2019 @yang.com Corporation Limited.
@contact: 659706575@qq.com
@software: made@Yang
@file: urls.py
@time: 2018/11/7 0007 8:00
@desc:
'''
from django.urls import path

from backstage import views

urlpatterns = [
    path('port/',views.show_index,name='index'),
    path('components/',views.show_components,name='components'),
    path('forms/',views.show_forms,name='forms'),
    path('tables/',views.show_tables,name='tables'),
    path('notification/',views.show_notification,name='notification'),
    path('typography/',views.show_typography,name='typography'),
    path('icon/',views.show_icons,name='icons')
]










