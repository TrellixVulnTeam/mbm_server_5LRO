# Generated by Django 3.2.8 on 2021-10-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0030_auto_20211029_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lotki_date_received',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='lotki_date_signed',
            field=models.DateField(default=None, null=True),
        ),
    ]
