from django.contrib import admin
from django.urls import path

from apis.viewsets import ObtainJWTView, CustomerViewSet, DeliveryViewSet, RequestViewSet, RequestList, RequestAnswerList, RequestAnswerViewSet, RequestUpdateViewSet
from deliveries.views import Index

urlpatterns = [
	path('', Index),
    path('admin/', admin.site.urls),
    path(r'login/', ObtainJWTView.as_view()),
    path(r'sign_up/customer/', CustomerViewSet.as_view()),
    path(r'sign_up/delivery/', DeliveryViewSet.as_view()),
    path(r'request/update/<int:pk>/<int:state>', RequestUpdateViewSet.as_view()),
    path(r'request/deliveries/', RequestViewSet.as_view()),
    path(r'request/list/', RequestList.as_view()),
    path(r'request_answer/', RequestAnswerViewSet.as_view()),
    path(r'request_answer/list/<int:pk>', RequestAnswerList.as_view()),
]