from django.db import models
from django.contrib.auth.models import User


CEDULA = 'CE'
TARJETA_IDENTIDAD = 'TI'
CEDULA_EXTRANJERA = 'CE'

DOCUMENT_CHOICES = (
    (CEDULA, 'Cedula'),
    (TARJETA_IDENTIDAD, 'Tarjeta de identidad'),
    (CEDULA_EXTRANJERA, 'Cedula Extranjera'),
)

CUSTOMER = 'CL'
DELIVERY = 'RE'

USER_CHOICES = (
    (CUSTOMER,'cliente'),
    (DELIVERY, 'repartidor'),
)


class Customer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text='Enlace al usuario',
        verbose_name='Usuario'
    )
    user_type = models.CharField(
        'Tipo de usuario',
        max_length=20,
        choices=USER_CHOICES,
        default=CUSTOMER
    )
    cellphone = models.CharField(
        'Telefono',
        max_length=15
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=15,
        choices=DOCUMENT_CHOICES,
        default=CEDULA,
    )
    document_number = models.CharField(
        'Documento de identidad',
        max_length=15,
        null=True
    )


    class Meta:

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return '%s %s %s' % (self.user.first_name, self.cellphone, self.user.email)


class Delivery(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text='Enlace al usuario',
        verbose_name='Usuario'
    )
    user_type = models.CharField(
        'Tipo de usuario',
        max_length=20,
        choices=USER_CHOICES,
        default=DELIVERY
    )
    cellphone = models.CharField(
        'Telefono',
        max_length=15
    )
    address = models.CharField(
        'Dirección',
        max_length=30
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=20,
        choices=DOCUMENT_CHOICES,
        default=CEDULA,
    )
    document_number = models.CharField(
        'Numero de documento',
        max_length=15,
        null=True
    )

    class Meta:

        verbose_name='Repartidor'
        verbose_name_plural='Repartidores'


    def __str__(self):
        return '%s %s %s' % (self.user.username, '--', self.document_number)
