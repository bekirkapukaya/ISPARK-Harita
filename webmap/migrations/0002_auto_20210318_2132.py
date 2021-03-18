# Generated by Django 3.1.7 on 2021-03-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ispark',
            name='lat',
            field=models.CharField(max_length=50, null=True, verbose_name='Boylam'),
        ),
        migrations.AlterField(
            model_name='ispark',
            name='lon',
            field=models.CharField(max_length=50, null=True, verbose_name='Enlem'),
        ),
        migrations.AlterField(
            model_name='ispark',
            name='point',
            field=models.CharField(max_length=100, null=True, verbose_name='Enlem/Boylam'),
        ),
        migrations.AlterField(
            model_name='ispark',
            name='polygon',
            field=models.CharField(max_length=15000, null=True, verbose_name='Polygon Verisi'),
        ),
    ]