# Generated by Django 3.0.7 on 2020-06-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200622_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userImg',
            field=models.ImageField(blank=True, default='colin.jpg', null=True, upload_to=''),
        ),
    ]