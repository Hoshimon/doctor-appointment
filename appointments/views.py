from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Doctor
from .models import Appointment
from .models import Specialty
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User

class CreateAppointment(CreateView):
	template_name = 'appointment_form.html'
	model = Appointment
	fields = '__all__'
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return super(CreateAppointment, self).form_valid(form)

create_appointment = CreateAppointment.as_view()

class RegisterDoctor(CreateView):
	template_name = 'doctor_form.html'
	model = Doctor
	fields = '__all__'
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return super(RegisterDoctor, self).form_valid(form)

register_doctor = RegisterDoctor.as_view()

class RegisterSpecialty(CreateView):
	template_name = 'specialty_form.html'
	model = Specialty
	fields = '__all__'
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return super(RegisterSpecialty, self).form_valid(form)

register_specialty = RegisterSpecialty.as_view()
