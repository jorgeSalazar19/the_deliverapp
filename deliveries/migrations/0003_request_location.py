# Generated by Django 2.0.6 on 2018-09-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0002_auto_20180919_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='location',
            field=models.CharField(blank=True, max_length=50, verbose_name='Ubicación'),
        ),
    ]
