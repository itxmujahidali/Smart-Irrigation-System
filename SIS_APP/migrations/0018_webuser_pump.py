# Generated by Django 4.0.3 on 2022-06-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIS_APP', '0017_alter_sensor_moistuer_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webuser',
            name='pump',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
