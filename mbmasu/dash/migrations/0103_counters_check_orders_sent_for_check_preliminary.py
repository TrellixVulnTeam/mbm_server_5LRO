# Generated by Django 3.2.8 on 2021-11-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0102_auto_20211122_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='counters',
            name='check_orders_sent_for_check_preliminary',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
