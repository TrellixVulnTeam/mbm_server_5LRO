# Generated by Django 3.2.8 on 2021-10-22 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20211022_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='sun_of_appliance',
            new_name='sum_of_appliance',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='dash.orderstatus'),
        ),
    ]
