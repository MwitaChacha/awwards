# Generated by Django 3.2.9 on 2021-12-14 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]