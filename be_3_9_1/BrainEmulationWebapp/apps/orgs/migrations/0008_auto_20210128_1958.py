# Generated by Django 3.1.5 on 2021-01-28 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0007_auto_20210128_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='org',
            options={'ordering': ('-team_size',)},
        ),
    ]
