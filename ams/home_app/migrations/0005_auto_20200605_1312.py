# Generated by Django 3.0.6 on 2020-06-05 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_auto_20200605_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='sname',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='sroll',
        ),
    ]