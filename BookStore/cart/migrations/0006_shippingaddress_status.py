# Generated by Django 4.0 on 2022-06-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_shippingaddress_purchased_books_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
