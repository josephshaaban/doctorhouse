# Generated by Django 2.2 on 2021-05-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_clinic', '0002_article_short_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='article_images'),
        ),
    ]
