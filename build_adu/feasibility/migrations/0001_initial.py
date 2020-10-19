# Generated by Django 3.1.2 on 2020-10-19 00:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcels',
            fields=[
                ('tlid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Tax Lot ID')),
                ('prim_accnum', models.CharField(max_length=50, verbose_name='Parcel Primary Account Number')),
                ('alt_accnum', models.CharField(max_length=50, verbose_name='Parcel Alternative Account Number')),
                ('site_address', models.CharField(max_length=60, verbose_name='Site Address from Tax Lot Records')),
                ('site_city', models.CharField(max_length=50, verbose_name='City from Tax Lot Records')),
                ('site_zip', models.CharField(max_length=50, verbose_name='Zip Code from Tax Lot Records')),
                ('land_val', models.IntegerField(verbose_name='Assessed Land Value')),
                ('bldg_val', models.IntegerField(verbose_name='Assessed Building Value')),
                ('total_val', models.IntegerField(verbose_name='Total Assessed Value')),
                ('parcel_bldg_sqft', models.FloatField(verbose_name='Building Sqft from Tax Lot Records')),
                ('a_t_acres', models.FloatField(verbose_name='Assessed Acres from Tax Lot Records')),
                ('year_built', models.IntegerField(verbose_name='Year Built from Tax Lot Records')),
                ('sale_date', models.CharField(max_length=50)),
                ('sale_price', models.IntegerField(verbose_name='Last Sale Price from Tax Lot Records')),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=2913)),
                ('index_right', models.FloatField(verbose_name='Index from join needs to be dropped')),
                ('bldg_id', models.CharField(max_length=50)),
                ('state_id', models.CharField(max_length=50)),
                ('bldg_num', models.FloatField(verbose_name='Building Number from Buildings Layer')),
                ('bldg_address', models.CharField(max_length=50, verbose_name='Address from Buildings Layer')),
                ('buildings_bldg_sqft', models.FloatField(verbose_name='Building Sqft from Buildings Layer')),
                ('n_stories', models.FloatField()),
                ('n_units', models.FloatField()),
                ('buildings_year_built', models.FloatField(verbose_name='Year Built from Buildings Layer')),
                ('bldg_footprint', models.FloatField(verbose_name='Building Footprint (SQFT)')),
                ('parcel_sqft', models.FloatField(verbose_name='Parcel SQFT')),
                ('geoid', models.CharField(max_length=25, verbose_name='Block Group FIPS Code')),
                ('one_bed_rent_sf', models.FloatField(verbose_name='Estimated One Bedroom Rent/SF')),
                ('two_bed_rent_sf', models.FloatField(verbose_name='Estimated Two Bedroom Rent/SF')),
            ],
        ),
    ]
