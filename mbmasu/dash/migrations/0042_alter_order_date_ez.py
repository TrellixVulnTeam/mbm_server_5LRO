# Generated by Django 3.2.8 on 2021-11-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0041_alter_order_date_ez'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_EZ',
            field=models.DateField(null=True),
        ),
    ]
