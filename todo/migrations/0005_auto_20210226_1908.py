# Generated by Django 3.1.4 on 2021-02-26 22:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210226_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 26, 22, 8, 51, 204283, tzinfo=utc), verbose_name='Fecha'),
        ),
    ]
