# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime   #formating and getting timestamps
from django.db import models
import re, bcrypt   # for hashing passwords and validations
# Create your models here.

USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-z A-Z]+$')

class UserManager(models.Manager):
	def registration_validation(self, registration_data):
		is_valid=True
		errors={}
		new_registration=[]
		if (len(registration_data['username'])<2):
			errors['username']="Username must be at least 2 characters long"
			is_valid=False
		elif not USERNAME_REGEX.match(registration_data['username']):
			errors['username']="Username must contain only letters or numbers"
			is_valid=False
		elif (User.objects.filter(username=registration_data['username']).exists()):
			errors['username']="Username already taken, please select a different one"
			is_valid=False
		if (len(registration_data['password']))<2:
			errors['password']="Password must be at least 2 characters long"
			is_valid=False
		elif registration_data['password'] != registration_data['confirm_password']:
			errors['password']="Passwords must match"
			is_valid=False
		if (len(registration_data['name']))<2:
			errors['name']="Name must be at least 2 characters long"
			is_valid=False
		elif not NAME_REGEX.match(registration_data['name']):
			errors['name']="Name must contain only letters and spaces"
			is_valid=False
		if (len(registration_data['email']))<2:
			errors['email']="Please enter an e-mail"
			is_valid=False
		elif not EMAIL_REGEX.match(registration_data['email']):
			errors['email']="E-mail must be in standard format - name@host.com"
			is_valid=False
		if is_valid:
			new_registration = User.objects.create(
				username=registration_data['username'],
				password=bcrypt.hashpw(registration_data['password'].encode(), bcrypt.gensalt()),
				name=registration_data['name'],
				email=registration_data['email'],)
			new_registration.save()
		return [is_valid, errors, new_registration]

	def login_validation(self, login_data):
		is_valid=True
		errors={}
		user=[]
		if len(login_data['username'])<2:
			errors['username']="Please enter a username that is atleast 2 characters long"
			is_valid=False
		elif len(login_data['password'])<2:
			errors['password']="Please enter a password longer than 2 characters"
			is_valid=False
		elif not User.objects.filter(username=login_data['username']).exists():
			errors['login_fail']="Username/password combination incorrect"
			is_valid=False
		elif not bcrypt.checkpw(login_data['password'].encode(), User.objects.get(username=login_data['username']).password.encode()):
			errors['login_fail']="Username/password combination incorrect"
			is_valid=False
		if is_valid:
			user=User.objects.get(username=login_data['username'])
		return [is_valid, errors, user]

	def all_users(self):
		users=User.objects.all()
		return users

	def delete_user(self, user_id):
		user=User.objects.get(id=user_id)
		user.delete()
		return True

class User(models.Model):
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
	def __repr__(self):
		return '<User: {}>'.format(self.username)