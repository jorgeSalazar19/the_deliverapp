from django.contrib import admin
from django.urls import path

from apis.viewsets import ObtainJWTView, CustomerViewSet, DeliveryViewSet, RequestViewSet, RequestList
from deliveries.views import Index

urlpatterns = [
	path('', Index),
    path('admin/', admin.site.urls),
    path(r'login/', ObtainJWTView.as_view()),
    path(r'sign_up/customer/', CustomerViewSet.as_view()),
    path(r'sign_up/delivery/', DeliveryViewSet.as_view()),
    path(r'request/deliveries/', RequestViewSet.as_view()),
    path(r'request/list/', RequestList.as_view()),
]