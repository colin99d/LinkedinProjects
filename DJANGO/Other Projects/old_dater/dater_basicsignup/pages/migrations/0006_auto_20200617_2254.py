# Generated by Django 3.0.7 on 2020-06-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200617_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
