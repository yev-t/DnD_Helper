# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(request, 'Login/index.html')

def register_user(request):
	pass

def login_user(request):
	pass