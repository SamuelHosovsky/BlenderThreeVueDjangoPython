# Generated by Django 3.1.5 on 2021-01-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0008_auto_20210128_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
