# Generated by Django 3.1.5 on 2021-01-23 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0004_auto_20210122_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orgs', to='orgs.category'),
        ),
    ]
