# Generated by Django 3.0.7 on 2020-06-18 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200617_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
