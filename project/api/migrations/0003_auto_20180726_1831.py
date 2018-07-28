# Generated by Django 2.0.7 on 2018-07-26 18:31

import colorfield.fields
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20180720_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalNation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.SlugField(help_text='Canonical name, should not include any epithets, must be unique', max_length=20)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('aliases', models.TextField(blank=True, help_text='CSV of alternative names this state may be known by')),
                ('description', models.TextField(blank=True, help_text='Flavor text, brief history, etc.')),
                ('wikipedia', models.URLField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical nation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTerritory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('geo', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical territory',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(
            model_name='nation',
            name='local_name',
        ),
        migrations.AddField(
            model_name='nation',
            name='aliases',
            field=models.TextField(blank=True, help_text='CSV of alternative names this state may be known by'),
        ),
        migrations.AddField(
            model_name='nation',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
        migrations.AddField(
            model_name='nation',
            name='description',
            field=models.TextField(blank=True, help_text='Flavor text, brief history, etc.'),
        ),
        migrations.AlterField(
            model_name='nation',
            name='name',
            field=models.SlugField(help_text='Canonical name, should not include any epithets, must be unique', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='nation',
            name='wikipedia',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalterritory',
            name='nation',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.Nation'),
        ),
    ]
