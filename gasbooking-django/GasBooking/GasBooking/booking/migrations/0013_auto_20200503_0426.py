# Generated by Django 3.0.5 on 2020-05-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20200503_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='email',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]
