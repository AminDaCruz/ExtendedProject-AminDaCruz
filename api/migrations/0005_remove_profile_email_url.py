# Generated by Django 4.0 on 2022-09-19 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_profile_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_url',
        ),
    ]