# Generated by Django 4.2.11 on 2024-03-26 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_blogmodel_user_alter_blogmodel_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='user',
        ),
    ]
