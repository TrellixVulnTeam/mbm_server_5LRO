# Generated by Django 3.2.8 on 2021-11-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0118_auto_20211129_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='check_after_temp_stop_files_uploaded',
        ),
    ]
