from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Specialty
from .models import Doctor
from .models import Appointment

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RegisterDoctorForm(ModelForm):
	choices = tuple(Specialty.objects.all().values_list())
	specialty = forms.ChoiceField(choices=choices)

	class Meta:
		model = Doctor
		exclude = ['specialty']
