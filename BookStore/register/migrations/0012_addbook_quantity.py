# Generated by Django 4.0.1 on 2022-06-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_addbook_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbook',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
