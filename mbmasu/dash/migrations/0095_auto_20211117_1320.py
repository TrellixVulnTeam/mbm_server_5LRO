# Generated by Django 3.2.8 on 2021-11-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0094_rename_new_orders_check_is_needed_countersadmin_new_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='lotki_preliminary_refuse_date_received',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lotki_preliminary_refuse_date_signed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
