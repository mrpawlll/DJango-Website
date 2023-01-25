from django.urls import path

from . import views


app_name = 'deliveryorder'

urlpatterns =[
    # /deliveryorder/
    path('create/',views.createDeliveryOrder,name='createDeliveryOrder'),
    path('',views.index,name='index'),
    path('<int:deliveryOrderID>/',views.details,name='details'),
]