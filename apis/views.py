from django.shortcuts import render
from users.models import Customer, Delivery

def jwt_response_payload_handler(token, user=None, request=None):

    try:
        user = Customer.objects.get(user=user)
    except:
        user = Delivery.objects.get(user=user)
    

    return {
        'token': token,
        'user': {
             'user_id': user.id,
             'user_type': user.user_type,
             'username': user.user.username,
             'email': user.user.email,
             'full_name': '%s %s' % (user.user.first_name, user.user.last_name),
             'cellphone': user.cellphone
        }

 }