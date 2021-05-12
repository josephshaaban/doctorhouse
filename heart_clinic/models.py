from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        null=False, blank=False,
    )
    content = models.CharField(
        max_length=1200,
        null=False, blank=False,
    )
    short_content = models.CharField(
        max_length=200,
        null=False, blank=False,
    )
    date = models.DateField(
        auto_now_add=True,
        null=False,
    )
    visit_count = models.PositiveIntegerField(
        default=0, null=False, blank=False,
    )
    image = models.ImageField(upload_to='article_images')
