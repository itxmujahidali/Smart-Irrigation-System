# Generated by Django 4.0.3 on 2022-06-09 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SIS_APP', '0014_sensor_sensorid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='sensorID',
            new_name='sensorkey',
        ),
    ]
