# Generated by Django 3.2.8 on 2021-11-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0049_auto_20211103_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_EZ',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lotki_refuse_date_received',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lotki_refuse_date_signed',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lotki_temp_stop_date_received',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lotki_temp_stop_date_signed',
            field=models.DateField(null=True),
        ),
    ]
