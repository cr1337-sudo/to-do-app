# Generated by Django 3.1.4 on 2021-02-26 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210226_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.date(2021, 2, 26), verbose_name='Fecha'),
        ),
    ]
