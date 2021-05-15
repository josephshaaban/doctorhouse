from captcha.fields import CaptchaField
from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField


class HeartConsultation(forms.Form):
    full_name = forms.CharField(label=_('Full name'), max_length=100)
    email = forms.EmailField()
    consultation_title = forms.CharField(label=_('Consultation title'), max_length=100)
    phone_number = PhoneNumberField()
    age = forms.IntegerField(max_value=150, min_value=1)
    gender = forms.ChoiceField(choices=(
        (0, _('male')),
        (1, _('female')),
    ))
    medical_history = forms.CharField(
        max_length=2000,
        min_length=100,
    )
    consultation_description = forms.CharField(
        max_length=2000,
        min_length=100,
    )
    captcha = CaptchaField()
    # todo: use captcha

