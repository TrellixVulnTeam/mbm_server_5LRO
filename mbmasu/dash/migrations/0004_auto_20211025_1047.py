# Generated by Django 3.2.8 on 2021-10-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20211022_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applier',
            name='category',
        ),
        migrations.AddField(
            model_name='order',
            name='aim',
            field=models.TextField(blank=True, null=True),
        ),
    ]
