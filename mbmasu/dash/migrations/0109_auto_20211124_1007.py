# Generated by Django 3.2.8 on 2021-11-24 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0108_auto_20211124_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkpreliminaryfiletocheckfinal',
            name='responsible_expert',
        ),
        migrations.RemoveField(
            model_name='checkpreliminaryfiletocheckreturned',
            name='responsible_expert',
        ),
    ]
