# Generated by Django 3.2.8 on 2021-11-03 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0052_auto_20211103_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationrefuse',
            name='refuse',
        ),
        migrations.RemoveField(
            model_name='notificationtempstop',
            name='temp_stop',
        ),
        migrations.RemoveField(
            model_name='refuse',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tempstop',
            name='id',
        ),
        migrations.AddField(
            model_name='refuse',
            name='notification',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dash.notificationrefuse'),
        ),
        migrations.AddField(
            model_name='tempstop',
            name='notification',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dash.notificationtempstop'),
        ),
    ]
