from django.contrib import admin
from .models import ( 
    observation
)

@admin.register(observation)
class observationAdmin(admin.ModelAdmin):
    model = observation
    list_display = ['name', 'mail', 'subject', 'message']
