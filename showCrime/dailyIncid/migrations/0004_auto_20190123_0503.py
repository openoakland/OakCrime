# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-23 05:03
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyIncid', '0003_auto_20170630_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensusTract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statefp', models.CharField(max_length=2)),
                ('countyfp', models.CharField(max_length=3)),
                ('tractce', models.CharField(max_length=6)),
                ('affgeoid', models.CharField(max_length=20)),
                ('geoid', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=100)),
                ('lsad', models.CharField(max_length=2)),
                ('aland', models.BigIntegerField()),
                ('awater', models.BigIntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4269)),
            ],
        ),
        migrations.CreateModel(
            name='OPDBeatMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('objectid', models.CharField(max_length=254)),
                ('cp_beat', models.CharField(max_length=254)),
                ('pol_beat', models.CharField(max_length=254)),
                ('pol_dist', models.CharField(max_length=254)),
                ('pol_sect', models.CharField(max_length=254)),
                ('beatid', models.CharField(max_length=254)),
                ('acres', models.CharField(max_length=254)),
                ('shape_area', models.CharField(max_length=254)),
                ('shape_len', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='callout',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='dlogData',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='gswP',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='lossList',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='ncustody',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='nhospital',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='nsuspect',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='nvictim',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='pcList',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='precinct',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='roList',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oakcrime',
            name='weapon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
