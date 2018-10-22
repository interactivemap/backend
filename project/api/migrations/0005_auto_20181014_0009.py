# Generated by Django 2.1.2 on 2018-10-14 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181011_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='name',
            field=models.TextField(help_text='Canonical name, which should not include any epithets and must be unique', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalentity',
            name='name',
            field=models.TextField(db_index=True, help_text='Canonical name, which should not include any epithets and must be unique', max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalpoliticalentity',
            name='name',
            field=models.TextField(db_index=True, help_text='Canonical name, which should not include any epithets and must be unique', max_length=100),
        ),
    ]
