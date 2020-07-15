# Generated by Django 3.0.5 on 2020-05-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('custno', models.CharField(max_length=10)),
                ('custoname', models.CharField(max_length=50)),
                ('b_date', models.CharField(max_length=12)),
                ('d_date', models.CharField(max_length=12)),
                ('ctype', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
