# Generated by Django 3.0.7 on 2020-06-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200622_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userImg',
            field=models.ImageField(blank=True, default='uploads/colin.jpg', null=True, upload_to=''),
        ),
    ]
