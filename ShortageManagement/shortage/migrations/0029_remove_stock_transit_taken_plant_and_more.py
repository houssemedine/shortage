# Generated by Django 4.0.2 on 2022-05-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0028_remove_zpp_md_stock_mrp_element_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_transit',
            name='taken_plant',
        ),
        migrations.AddField(
            model_name='stock_transit',
            name='division',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
