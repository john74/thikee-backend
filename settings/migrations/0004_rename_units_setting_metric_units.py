# Generated by Django 4.2.3 on 2023-07-21 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_setting_timezone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='units',
            new_name='metric_units',
        ),
    ]
