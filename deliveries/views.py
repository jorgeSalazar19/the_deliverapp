from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from .models import observation

def Index(request):

    if request.method == 'GET':
        template = loader.get_template('index.html')
        msg = (False,'')
        ctx = {
            'mensaje' : msg
        }
        return HttpResponse(template.render(ctx,request))

    elif request.method == 'POST':

        name = request.POST.get('name')
        mail = request.POST.get('mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Observation = observation(
            name=name, 
            mail=mail, 
            subject=subject, 
            message=message
        )

        Observation.save()

        msg = (True, 'Su comentario se ha enviado con exito')

        template = loader.get_template('index.html')
        ctx = {
            'mensaje' : msg
        }
        return HttpResponse(template.render(ctx,request))

