# Generated by Django 3.0.5 on 2020-05-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20200503_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='type',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]