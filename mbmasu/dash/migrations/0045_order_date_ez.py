# Generated by Django 3.2.8 on 2021-11-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0044_remove_order_date_ez'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_EZ',
            field=models.DateField(default=None, null=True),
        ),
    ]
