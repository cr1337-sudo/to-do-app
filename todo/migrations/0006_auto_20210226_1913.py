# Generated by Django 3.1.4 on 2021-02-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210226_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
