# Generated by Django 3.0.6 on 2020-06-06 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0013_auto_20200606_1159'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('date', 'sroll', 'status')},
        ),
    ]
