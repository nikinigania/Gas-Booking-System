# Generated by Django 3.0.5 on 2020-05-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='photo',
            field=models.ImageField(default='', upload_to='profile'),
        ),
    ]
