from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('heart_clinic', views.heart_clinic, name='heart_clinic'),
]