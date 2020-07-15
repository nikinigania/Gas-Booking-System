# Generated by Django 3.0.5 on 2020-05-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cylindertype', models.CharField(max_length=10)),
                ('connectiondate', models.DateField(auto_now=True)),
                ('custname', models.CharField(max_length=50)),
                ('custadd', models.CharField(max_length=50)),
                ('custcity', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
    ]
