# Generated by Django 3.1.5 on 2021-01-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0002_auto_20210122_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='website',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
