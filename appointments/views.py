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
from forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib import messages
from django.forms import ModelForm
from django import forms
from forms import RegisterDoctorForm

class CreateAppointment(CreateView):
	template_name = 'appointment_form.html'
	model = Appointment
	fields = '__all__'
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(CreateAppointment, self).form_valid(form)

create_appointment = CreateAppointment.as_view()

class RegisterDoctor(CreateView):
	template_name = 'doctor_form.html'
	form_class = RegisterDoctorForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(RegisterDoctor, self).form_valid(form)

register_doctor = RegisterDoctor.as_view()

class RegisterSpecialty(CreateView):
	template_name = 'specialty_form.html'
	model = Specialty
	fields = '__all__'
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(RegisterSpecialty, self).form_valid(form)

register_specialty = RegisterSpecialty.as_view()

class AppointmentList(ListView):
	model = Appointment
	template_name = 'appointment_list.html'
	def get_context_data(self, **kwargs):
		context = super(AppointmentList, self).get_context_data(**kwargs)
		return context
appointment_list = AppointmentList.as_view()

def AddingUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, "You are now registered and logged in.")
            login(request, new_user)
            return HttpResponseRedirect('/')
    else:
        form = UserForm()

    return render(request, 'adduser.html', {'form': form})

class AppointmentEdit(UpdateView):
	model = Appointment
	template_name = "appointment_form.html"
	success_url = reverse_lazy('appointment_list')
	fields = '__all__'
	def get_object(self, queryset=None):
		obj = super(AppointmentEdit, self).get_object()
		return obj

appointment_edit = AppointmentEdit.as_view()

class AppointmentDelete(DeleteView):
	model = Appointment
	template_name = "appointment_delete.html"
	success_url = reverse_lazy('appointment_list')
	def get_object(self, queryset=None):
		obj = super(AppointmentDelete, self).get_object()
		return obj

appointment_delete = AppointmentDelete.as_view()
