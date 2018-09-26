from django.contrib import admin
from .models import (
    Request
)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
	model = Request
	list_display = ['willing_pay']