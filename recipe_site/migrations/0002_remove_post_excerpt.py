# Generated by Django 3.2.21 on 2023-09-26 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
    ]
