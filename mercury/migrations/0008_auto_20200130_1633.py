# Generated by Django 2.2.9 on 2020-01-30 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercury', '0007_auto_20200130_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windspeedsensor',
            old_name='wind_speed',
            new_name='current_wind_speed',
        ),
    ]
