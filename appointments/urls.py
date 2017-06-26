from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^create_appointment/', views.create_appointment, name = 'create_appointment'),
	url(r'^register_doctor/', views.register_doctor, name = 'register_doctor'),
	url(r'^register_specialty/', views.register_specialty, name = 'register_specialty'),
	url(r'^see_appointments/', views.appointment_list, name = 'appointment_list'),
	url(r'^create_user/', views.AddingUser),
	url(r'^(?P<pk>[-\d]+)/edit/$', views.appointment_edit, name='appointment_edit'),
	url(r'^(?P<pk>[-\d]+)/delete/$', views.appointment_delete, name='appointment_delete'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
