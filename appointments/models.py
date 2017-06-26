# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Doctor(models.Model):
	name = models.CharField(max_length=200)
	specialty = models.CharField(max_length=200)

	class Meta:
		ordering = ('id',)

class Specialty(models.Model):
	specialty_name = models.CharField(max_length=200)

class Appointment(models.Model):
	doctor = models.CharField(max_length=200)
	description = models.TextField(max_length=10000)
	date = models.DateField()

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.user.username
