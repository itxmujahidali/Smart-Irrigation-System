# Generated by Django 4.0.3 on 2022-05-31 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIS_APP', '0007_auto_20210928_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='webuser',
            name='recovery_code',
            field=models.CharField(default=1234, max_length=4),
            preserve_default=False,
        ),
    ]
