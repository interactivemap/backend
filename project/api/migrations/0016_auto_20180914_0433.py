# Generated by Django 2.0.7 on 2018-09-14 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20180912_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diplomaticrelation',
            old_name='child_party',
            new_name='child_parties',
        ),
        migrations.RenameField(
            model_name='diplomaticrelation',
            old_name='parent_party',
            new_name='parent_parties',
        ),
    ]