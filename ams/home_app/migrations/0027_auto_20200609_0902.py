# Generated by Django 3.0.6 on 2020-06-09 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0026_auto_20200609_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='tattendance',
            name='date',
            field=models.CharField(default='', max_length=25),
        ),
    ]
