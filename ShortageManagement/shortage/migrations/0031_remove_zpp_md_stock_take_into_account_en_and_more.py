# Generated by Django 4.0.2 on 2022-05-23 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0030_alter_stock_transit_division'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='take_into_account_en',
        ),
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='take_into_account_fr',
        ),
    ]
