# Generated by Django 4.0.2 on 2022-02-18 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mb52_for_free_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mb52',
            name='blocked',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='blocked_return_stock_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='blocked_stock_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='currency',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='in_quality_control',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='non_free_stock',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='non_free_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='returns',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='store',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='store_level_deletion_indicator',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='transit_transfer',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='transit_transfer_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='unit',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='value_free_use',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mb52',
            name='value_quality_control',
            field=models.FloatField(null=True),
        ),
    ]
