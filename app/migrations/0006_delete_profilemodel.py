# Generated by Django 4.2.11 on 2024-03-26 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_blogmodel_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileModel',
        ),
    ]
