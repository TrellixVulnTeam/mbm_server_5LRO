# Generated by Django 3.2.8 on 2021-11-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0046_auto_20211103_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_EZ_ww',
            field=models.DateField(default=None, null=True),
        ),
    ]
