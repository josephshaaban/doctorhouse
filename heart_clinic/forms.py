from django import forms
from django.utils.translation import gettext_lazy as _


class HeartConsultation(forms.Form):
    full_name = forms.CharField(label=_('Full name'), max_length=100)
    email = forms.EmailField()
    consultation_title = forms.CharField(label=_('Consultation title'), max_length=100)

