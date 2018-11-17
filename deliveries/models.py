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

PENDING = 'pendiente'
DONE = 'realizada'
PROCESS = 'proceso'

STATE_CHOICES = (
    (PENDING, 'Pendiente'),
    (PROCESS, 'En proceso'),
    (DONE, 'Realizada'),
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
    state = models.CharField(
        'Estado',
        max_length=20,
        choices=STATE_CHOICES,
        default = PENDING
    )

    def data_customer(self):
        return str(self.customer)

    def __str__(self):
        return '%s %s %s' % (self.customer, ',',  self.type)

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"

class RequestAnswer(models.Model):

    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        verbose_name='Repartidor'
    )
    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        verbose_name='Solicitud'
    )
    offer_price = models.CharField(
        'Precio de oferta',
        max_length=50
    )
    description = models.TextField(
        'Descripción de oferta',
        max_length=200
    )
    state = models.CharField(
        'Estado',
        max_length=20,
        choices=STATE_CHOICES
    )

    def data_delivery(self):
        return str(self.delivery)


class observation(models.Model):


    name=models.CharField(
        'Nombre',
        max_length=40
    )
    mail=models.EmailField(
        'Correo Electronico',
    )
    subject=models.CharField(
        'Asunto',
        max_length=40
    )
    message=models.TextField(
        'Mensaje',
        max_length=300
    )


    class Meta:
        verbose_name='Comentario'
        verbose_name_plural='Comentarios'


    def __str__(self):
        return '%s %s' % (self.name, self.mail)

