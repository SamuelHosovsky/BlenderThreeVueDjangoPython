# Generated by Django 3.1.5 on 2021-04-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0012_auto_20210413_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='primarily_concerned_with_brain_area',
            field=models.CharField(choices=[('frontal', 'Frontal lobe'), ('occipit', 'Occipital lobe'), ('cereb', 'Cerebellum'), ('temp', 'Temporal lobe'), ('pariet', 'Parietal lobe'), ('corpus', 'Corpus Callosum'), ('pitua', 'Pituitary gland'), ('stem', 'Brainstem')], max_length=7),
        ),
    ]
