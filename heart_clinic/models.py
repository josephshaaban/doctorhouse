from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Article(models.Model):
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=100,
        null=False, blank=False,
    )
    content = models.TextField(
        verbose_name=_('Content'),
        null=False, blank=False,
    )
    short_content = models.TextField(
        verbose_name=_('Short content'),
        null=False, blank=False,
    )
    date = models.DateField(
        verbose_name=_('Date'),
        auto_now_add=True,
        null=False,
    )
    visit_count = models.PositiveIntegerField(
        verbose_name=_('Visit count'),
        default=0, null=False, blank=False,
    )
    image = models.ImageField(upload_to='article_images')


class HeartConsultation(models.Model):
    class Meta:
        verbose_name = _('Heart consultation')
        verbose_name_plural = _('Heart consultations')

    full_name = models.CharField(verbose_name=_('Full name'), max_length=100)
    email = models.EmailField()
    consultation_title = models.CharField(verbose_name=_('Consultation title'), max_length=100)
    phone_number = PhoneNumberField()
    age = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(1)])
    gender = models.BooleanField(choices=(
        (True, _('male')),
        (False, _('female')),
    ))
    medical_history = models.TextField(
        verbose_name=_('Medical history'),
        null=False, blank=False,
    )
    consultation_description = models.TextField(
        verbose_name=_('Consultation description'),
        null=False, blank=False,
    )
