from django.contrib import admin
from .models import ( 
    observation,
    Request,
    RequestAnswer
)

@admin.register(observation)
class observationAdmin(admin.ModelAdmin):
    model = observation
    list_display = ['name', 'mail', 'subject', 'message']

@admin.register(Request)
class ResquestAdmin(admin.ModelAdmin):
	model = Request
	list_display = ['customer', 'description', 'willing_pay', 'state']

@admin.register(RequestAnswer)
class RequestAnswerAdmin(admin.ModelAdmin):
	model = RequestAnswer
	list_display = ['delivery', 'request', 'offer_price', 'description', 'state']
