# Generated by Django 3.2.8 on 2021-10-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0022_auto_20211029_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertypecheck',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
