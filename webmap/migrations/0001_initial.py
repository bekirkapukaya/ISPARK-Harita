# Generated by Django 3.1.7 on 2021-03-19 21:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ispark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkId', models.PositiveSmallIntegerField(verbose_name='Park ID')),
                ('parkName', models.CharField(max_length=100, verbose_name='Park Adı')),
                ('locationId', models.PositiveSmallIntegerField(verbose_name='Lokasyon ID')),
                ('locationCode', models.PositiveSmallIntegerField(verbose_name='Lokasyon Kodu')),
                ('locationName', models.CharField(max_length=100, verbose_name='Lokasyon Adı')),
                ('parkTypeId', models.PositiveSmallIntegerField(verbose_name='Park Tipi ID')),
                ('parkType', models.CharField(max_length=50, verbose_name='Park Tipi')),
                ('parkCapacity', models.PositiveSmallIntegerField(verbose_name='Park Kapasitesi')),
                ('workHours', models.CharField(max_length=300, verbose_name='Calışma Saatleri')),
                ('regionId', models.PositiveSmallIntegerField(verbose_name='Bölge ID')),
                ('region', models.CharField(max_length=50, verbose_name='Bölge')),
                ('subRegionId', models.PositiveSmallIntegerField(verbose_name='Alt Bölge ID')),
                ('subRegion', models.CharField(max_length=50, verbose_name='Alt Bölge')),
                ('boroughld', models.PositiveSmallIntegerField(verbose_name='İlçe ID')),
                ('borough', models.CharField(max_length=100, verbose_name='İlçe')),
                ('address', models.CharField(max_length=300, verbose_name='Adres')),
                ('point', models.CharField(max_length=100, null=True, verbose_name='Enlem/Boylam')),
                ('polygon', models.CharField(max_length=15000, null=True, verbose_name='Polygon Verisi')),
                ('lat', models.CharField(max_length=50, null=True, verbose_name='Boylam')),
                ('lon', models.CharField(max_length=50, null=True, verbose_name='Enlem')),
                ('monthlyPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Aylık Abonelik Ücreti')),
                ('freeParkingTime', models.PositiveSmallIntegerField(verbose_name='Ücretsiz Parklanma Süresi (dakika)')),
                ('price', models.CharField(max_length=700, verbose_name='Tarifesi')),
                ('parkAndGoPoint', models.PositiveSmallIntegerField(verbose_name='Park Et Devam Et Noktası')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Geometri')),
            ],
        ),
    ]
