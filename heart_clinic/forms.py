from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms

from heart_clinic.models import HeartConsultation


class HeartConsultationForm(forms.ModelForm):
    class Meta:
        model = HeartConsultation
        fields = '__all__'

    captcha = CaptchaField(widget=CaptchaTextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter captcha",
    }))
