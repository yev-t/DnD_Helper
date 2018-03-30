# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.

def index(request):
	if not request.session.get('user_id')==None:
		return render(request, 'Login/home.html')
	if request.session.get('validation')==None:
		request.session['form']=["active","inactive"]
	else:
		request.session['form']=["inactive","active"]
		request.session['validation']=None
	return render(request, 'Login/index.html')

def register_user(request):
	validate=User.objects.registration_validation(request.POST)
	if not validate[0]:
		for key in validate[1]:
			messages.error(request, validate[1][key])
			request.session['validation']=False
		return redirect('/')
	else:
		request.session['user_id']=validate[2].id
		request.session['name']=validate[2].name
		return redirect('my_home')

def login_user(request):
	validate=User.objects.login_validation(request.POST)
	if not validate[0]:
		for key in validate[1]:
			messages.error(request, validate[1][key])
		return redirect('/')
	else:
		request.session['user_id']=validate[2].id
		request.session['name']=validate[2].name
		return redirect('my_home')

def home(request):
	all_users=User.objects.all_users()
	request.session['all_users']=[]
	for user in all_users:
		context={
			'name':user.name,
			'user_id':user.id,
		}
		request.session['all_users'].append(context)
	return render(request, 'Login/home.html')

def logout(request):
	request.session['user_id']=None
	return redirect('/')

def delete_user(request):
	User.objects.delete_user(request.POST['user_id'])
	return redirect('my_home')
