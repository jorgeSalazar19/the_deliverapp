# Generated by Django 2.0.6 on 2018-09-19 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20180916_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_price', models.CharField(max_length=50, verbose_name='Mi precio')),
                ('description', models.CharField(blank=True, max_length=50, verbose_name='Descripcion')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Delivery')),
            ],
            options={
                'verbose_name_plural': 'Ofertas',
                'verbose_name': 'Oferta',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('willing_pay', models.CharField(max_length=50, verbose_name='Dispuesto a pagar')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Customer', verbose_name='Cliente')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deliveries.Offer', verbose_name='Oferta')),
            ],
            options={
                'verbose_name_plural': 'Solicitudes',
                'verbose_name': 'Solicitud',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Descripcion')),
                ('shipping_type', models.CharField(choices=[('MP', 'Realizar pagos'), ('CB', 'Transportar objetos'), ('OT', 'Otro')], default='CB', max_length=50, verbose_name='Tipo de envio')),
            ],
            options={
                'verbose_name_plural': 'Tipos',
                'verbose_name': 'Tipo',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveries.Type', verbose_name='Tipo'),
        ),
    ]
