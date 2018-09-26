# Generated by Django 2.0.6 on 2018-09-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0004_request_decription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='location',
        ),
        migrations.AddField(
            model_name='request',
            name='latitud',
            field=models.CharField(blank=True, max_length=25, verbose_name='latitud'),
        ),
        migrations.AddField(
            model_name='request',
            name='longitud',
            field=models.CharField(blank=True, max_length=25, verbose_name='longitud'),
        ),
    ]