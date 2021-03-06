# Generated by Django 2.0.6 on 2018-09-16 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone', models.CharField(max_length=15, verbose_name='Telefono')),
                ('document_type', models.CharField(choices=[('CE', 'Cedula'), ('TI', 'Tarjeta de identidad'), ('CE', 'Cedula Extranjera')], default='CE', max_length=15, verbose_name='Tipo de documento')),
                ('document_number', models.CharField(max_length=15, null=True, verbose_name='Documento de identidad')),
                ('user', models.OneToOneField(help_text='Enlace al usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone', models.CharField(max_length=15, verbose_name='Telefono')),
                ('address', models.CharField(max_length=30, verbose_name='Dirección')),
                ('document_type', models.CharField(choices=[('CE', 'Cedula'), ('TI', 'Tarjeta de identidad'), ('CE', 'Cedula Extranjera')], default='CE', max_length=20, verbose_name='Tipo de documento')),
                ('document_number', models.CharField(max_length=15, null=True, verbose_name='Numero de documento')),
                ('user', models.OneToOneField(help_text='Enlace al usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Repartidores',
                'verbose_name': 'Repartidor',
            },
        ),
    ]
