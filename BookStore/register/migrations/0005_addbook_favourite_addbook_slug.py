# Generated by Django 4.0 on 2022-05-24 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0004_alter_addbook_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbook',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addbook',
            name='slug',
            field=models.SlugField(blank=True, max_length=120),
        ),
    ]
