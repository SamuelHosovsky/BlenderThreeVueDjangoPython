# Generated by Django 3.1.5 on 2021-01-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0003_auto_20210122_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
