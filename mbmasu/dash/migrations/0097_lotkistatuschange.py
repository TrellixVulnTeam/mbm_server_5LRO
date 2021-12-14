# Generated by Django 3.2.8 on 2021-11-17 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash', '0096_order_refuse_after_temp_stop'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotkiStatusChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dash.order')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='dash.lotkicontent', verbose_name='Статус лотки')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
