# Generated by Django 3.2.8 on 2021-11-12 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0076_tempstop_end_date_after_temp_stop_for_subcontractor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempstop',
            name='end_date_after_temp_stop_for_subcontractor',
        ),
    ]
