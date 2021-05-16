from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.utils.translation import gettext_lazy as _

from heart_clinic.models import HeartConsultation, HeartConsultationSystem


class HeartConsultationForm(forms.ModelForm):
    class Meta:
        model = HeartConsultation
        fields = '__all__'

    captcha = CaptchaField(widget=CaptchaTextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter captcha",
    }))


class HeartConsultationSystemForm(forms.ModelForm):
    class Meta:
        model = HeartConsultationSystem
        exclude = ['disease']
        # labels = {
        #     'age': _('Age'),
        # }
        widgets = {
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Age'),
                }),
            'chest_pain_type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Chest pain type'),
                }),
            'rest_blood_pressure': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Rest blood pressure'),
                }),
            'blood_sugar': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Blood sugar'),
                }),
            'rest_electro': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Rest electro'),
                }),
            'max_heart_rate': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Max heart rate'),
                }),
            'exercice_angina': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Exercice angina'),
                }),
        }
        # help_texts = {
        #     'age': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'age': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

