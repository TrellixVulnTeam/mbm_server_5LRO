# Generated by Django 3.2.8 on 2021-11-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0112_auto_20211126_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='check_preliminary_pass_without_check',
            field=models.BooleanField(default=False, verbose_name='Предварительная проверка пропущена'),
        ),
    ]
