# Generated by Django 4.0.2 on 2022-05-23 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0021_remove_mb52_uploaded_at_remove_mb52_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='uploaded_at',
        ),
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='uploaded_by',
        ),
    ]
