# Generated by Django 3.0.5 on 2020-05-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_customer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
