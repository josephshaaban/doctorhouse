from django.contrib import admin

from heart_clinic.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """ Admin class for Article model """
