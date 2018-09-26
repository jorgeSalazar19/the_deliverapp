from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

def Index(request):
    template = loader.get_template('landing.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))