# Generated by Django 3.1.5 on 2021-04-13 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0014_auto_20210413_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='org',
            old_name='locations',
            new_name='all_locations',
        ),
    ]
