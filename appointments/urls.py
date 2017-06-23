from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^create_appointment/', views.create_appointment, name = 'create_appointment'),
	url(r'^register_doctor/', views.register_doctor, name = 'register_doctor'),
	url(r'^register_specialty/', views.register_specialty, name = 'register_specialty'),
]
