# Generated by Django 2.0.7 on 2018-10-08 20:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20180914_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalnation',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), blank=True, help_text='Alternative names this state may be known by', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='nation',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), blank=True, help_text='Alternative names this state may be known by', null=True, size=None),
        ),
    ]
