from django.contrib import admin
from .models import ( 
    Customer,
    Delivery
)


def correo_usuario(object):
  return object.user.email

def nombre_completo(object):
  return '%s %s' % (object.user.first_name, object.user.last_name)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['user', nombre_completo, 'document_number', correo_usuario]


@admin.register(Delivery)
class CustomerAdmin(admin.ModelAdmin):
    model = Delivery
    list_display = ['user', nombre_completo, 'document_number', correo_usuario]


