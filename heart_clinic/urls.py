from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('heart_clinic/', views.heart_clinic, name='heart_clinic'),
    path(
        'heart_adm_system/', views.heart_adm_system, name='heart_adm_system',
    ),
    path(
        'heart_adm_system/bayes/', views.heart_adm_system, name='heart_adm_system_bayes',
        kwargs={'method': 'bayes'},
    ),
    url(r'^send-email/(?P<pk>\d+)/$', views.SendEmail.as_view(), name='send-email'),
    path('thanks/', views.thanks, name='thanks'),
]
