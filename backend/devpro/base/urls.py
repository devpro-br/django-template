from django.urls import path

from devpro.base import views

urlpatterns = [
    path('', views.home, name='home'),
]
