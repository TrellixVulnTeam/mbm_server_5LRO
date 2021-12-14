# Generated by Django 3.2.8 on 2021-10-28 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash', '0018_auto_20211028_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='responsible_after_temp_stop',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='responsible_after_temp_stop', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='responsible_preliminary',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='responsible_preliminary', to=settings.AUTH_USER_MODEL),
        ),
    ]
