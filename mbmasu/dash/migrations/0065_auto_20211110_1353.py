# Generated by Django 3.2.8 on 2021-11-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0064_auto_20211110_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counters',
            name='admin_distribution_afetr_temp_stop',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='admin_distribution_preliminary',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='admin_orders_all',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='admin_remade_order_date',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='check_orders_checked_after_temp_stop',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='check_orders_checked_preliminary',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='check_orders_to_check_after_temp_stop',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='check_orders_to_check_preliminary',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='ez_doc',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='ez_doc_remake',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='ez_pdf',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='new_orders',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='refuse_by_date',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='refuse_by_docs',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='refuse_preliminary',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='statist_ez',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='statist_ez_on_signing',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='statist_refuse_on_signing',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='statist_refuses_not_preliminary',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='statist_temp_stop_on_signing',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='temp_stop_check',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='temp_stop_date',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='temp_stop_on_check',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='temp_stop_remade_order_date',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='temp_stop_remade_order_decision',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='temp_stop_with_notification',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counters',
            name='temp_stop_without_notification',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
