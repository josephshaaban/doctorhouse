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

    def __str__(self):
        return self.title


class HeartConsultation(models.Model):
    class Meta:
        verbose_name = _('Heart consultation')
        verbose_name_plural = _('Heart consultations')

    full_name = models.CharField(verbose_name=_('Full name'), max_length=100)
    email = models.EmailField(verbose_name=_('Email'))
    consultation_title = models.CharField(verbose_name=_('Consultation title'), max_length=100)
    phone_number = PhoneNumberField(verbose_name=_('Phone number'))
    age = models.IntegerField(
        verbose_name=_('Age'),
        validators=[MaxValueValidator(150), MinValueValidator(1)]
    )
    gender = models.BooleanField(
        verbose_name=_('Gender'),
        choices=(
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

    def __str__(self):
        return self.full_name


class HeartConsultationSystem(models.Model):
    class Meta:
        verbose_name = _('Heart consultation system')
        verbose_name_plural = _('Heart consultations system')

    age = models.IntegerField(
        verbose_name=_('Age'),
        validators=[MaxValueValidator(150), MinValueValidator(1)],
        null=False, blank=False,
    )
    chest_pain_type = models.CharField(
        verbose_name=_('Chest pain type'),
        max_length=32,
        null=False, blank=False,
        choices=(
            ('asympt', _('Asymptote')),
            ('atyp_angina', _('A typ angina')),
            ('typ_angina', _('typ angina')),
            ('non_anginal', _('Non anginal')),
        ))
    rest_blood_pressure = models.IntegerField(
        verbose_name=_('Rest blood pressure'),
        null=False, blank=False,
        validators=[MaxValueValidator(250), MinValueValidator(30)],
    )
    blood_sugar = models.CharField(
        verbose_name=_('Blood sugar'),
        max_length=32,
        null=False, blank=False,
        choices=(
            ('FALSE', _('False')),
            ('True', _('True')),
        ))
    rest_electro = models.CharField(
        verbose_name=_('Rest electro'),
        max_length=32,
        null=False, blank=False,
        choices=(
            ('normal', _('Normal')),
            ('left_vent_hyper', _('Left vent hyper')),
            ('st_t_wave_abnormality', _('st_t_wave_abnormality')),
        ))
    max_heart_rate = models.IntegerField(
        verbose_name=_('Max heart rate'),
        null=False, blank=False,
        validators=[MaxValueValidator(250), MinValueValidator(30)],
    )
    exercice_angina = models.CharField(
        verbose_name=_('Exercice angina'),
        max_length=32,
        null=False, blank=False,
        choices=(
            ('yes', _('Yes')),
            ('no', _('No')),
        ))
    disease = models.CharField(
        verbose_name=_('Disease'),
        max_length=32,
        choices=(
            ('positive', _('Positive')),
            ('negative', _('Negative')),
        ))
