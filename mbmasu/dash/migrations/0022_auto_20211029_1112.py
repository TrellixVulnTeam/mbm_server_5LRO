# Generated by Django 3.2.8 on 2021-10-29 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0021_order_lotki_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTypeCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='dash.ordertypecheck'),
        ),
    ]
