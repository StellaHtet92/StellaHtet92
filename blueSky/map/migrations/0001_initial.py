# Generated by Django 3.2.8 on 2021-11-11 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('photo', models.ImageField(upload_to='%Y/%m/%d')),
                ('uploaded_date', models.DateField(blank=True, default=datetime.date.today)),
            ],
        ),
    ]