from django.contrib import admin

from heart_clinic.models import Article, HeartConsultation, HeartConsultationSystem


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """ Admin class for Article model """
    list_display = [
        'title', 'date', 'visit_count'
    ]


@admin.register(HeartConsultation)
class HeartConsultationAdmin(admin.ModelAdmin):
    """ Admin class for HeartConsultation model """
    list_display = [
        'full_name', 'consultation_title'
    ]


@admin.register(HeartConsultationSystem)
class HeartConsultationSystemAdmin(admin.ModelAdmin):
    """ Admin class for HeartConsultationSystem model """
