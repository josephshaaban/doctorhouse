from django.contrib import admin

from heart_clinic.models import Article, HeartConsultation


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """ Admin class for Article model """


@admin.register(HeartConsultation)
class HeartConsultationAdmin(admin.ModelAdmin):
    """ Admin class for HeartConsultation model """
