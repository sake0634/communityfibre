# Generated by Django 4.0 on 2022-01-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_sap_inner_vlan_alter_sap_outer_vlan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_id_str',
            field=models.CharField(max_length=10),
        ),
    ]
