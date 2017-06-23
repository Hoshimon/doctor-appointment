from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html'), name = 'index'),
    url(r'^admin/', admin.site.urls),
	url(r'^appointments/', include('appointments.urls')),
]
