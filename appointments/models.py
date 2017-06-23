# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Doctor(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	doctor_name = models.CharField(max_length=200)
	doctor_address = models.CharField(max_length=200)
	doctor_office = models.CharField(max_length=200)

	class Meta:
		ordering = ('id',)

class Specialty(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	specialty_name = models.CharField(max_length=200)
	specialty_department = models.CharField(max_length=200)

class Appointment(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	doctor = models.CharField(max_length=200)
	office = models.CharField(max_length=200)
	specialty = models.CharField(max_length=200)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.user.username
