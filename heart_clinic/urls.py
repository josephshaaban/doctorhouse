from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('heart_clinic/', views.heart_clinic, name='heart_clinic'),
    path('heart_adm_system/', views.heart_adm_system, name='heart_adm_system'),
    path('thanks/', views.thanks, name='thanks'),
]
