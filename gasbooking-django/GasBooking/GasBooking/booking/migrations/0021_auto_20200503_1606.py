# Generated by Django 3.0.5 on 2020-05-03 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0020_auto_20200503_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='connection',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Status'),
        ),
    ]
