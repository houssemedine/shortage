# Generated by Django 4.0.2 on 2022-06-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0042_alter_z_sc_m_0002_num_material_fourn1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='z_sc_p_0004',
            name='updated_on',
            field=models.DateTimeField(null=True),
        ),
    ]
