# Generated by Django 3.2.6 on 2021-09-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIS_APP', '0002_auto_20210906_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='number_of_plants',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plant',
            name='number_of_sensors',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plant',
            name='planted_area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='schedulewater',
            name='water_flow',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='moistuer_level',
            field=models.IntegerField(),
        ),
    ]
