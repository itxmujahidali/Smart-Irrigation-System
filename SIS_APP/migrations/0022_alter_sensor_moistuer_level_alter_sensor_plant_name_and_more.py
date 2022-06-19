# Generated by Django 4.0.3 on 2022-06-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIS_APP', '0021_alter_webuser_contact_alter_webuser_farm_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='moistuer_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='plant_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensorkey',
            field=models.IntegerField(null=True),
        ),
    ]