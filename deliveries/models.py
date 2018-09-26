from django.db import models
from users.models import ( 
    Customer,
    Delivery
)


MAKE_PAYMENT = 'pago'
CARRY_OBJECT = 'domicilio'
OTHER = 'otro'

TYPE_CHOICES = (
    (MAKE_PAYMENT, 'Realizar pagos'),
    (CARRY_OBJECT, 'Transportar objetos'),
    (OTHER, 'Otro'),
)

    
class Request(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete = models.CASCADE,
        verbose_name='Cliente'
    )
    type = models.CharField(
    	'Tipo',
    	max_length=20,
        choices=TYPE_CHOICES,
    )
    description= models.CharField(
        'Descripcion',
        max_length=100,
        null=False,
        blank=True
    )
    willing_pay = models.CharField(
        'Dispuesto a pagar',
         max_length=50
    )
    latitud = models.CharField(
        'latitud',
        max_length=25,
        null=False,
        blank=True
    )
    longitud = models.CharField(
        'longitud',
        max_length=25,
        null=False,
        blank=True
    )

    def data_customer(self):
        return str(self.customer)


    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"