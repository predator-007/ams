# Generated by Django 3.0.6 on 2020-06-09 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0024_auto_20200608_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2020-06-09'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='sroll',
            field=models.CharField(default="' format", max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='ssec',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='tattendance',
            name='date',
            field=models.DateField(default='2020-06-09'),
        ),
    ]
