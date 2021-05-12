from django.db import models
from django.utils.translation import gettext_lazy as _


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
