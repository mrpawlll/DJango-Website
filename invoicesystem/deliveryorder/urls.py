from django.urls import path

from . import views


app_name = 'deliveryorder'

urlpatterns =[
    path('approveDOList/<int:deliveryorderid>/',views.approveDetails,name='approveDOdetails'),
    path('courierList/<int:deliveryorderid>/',views.courierDetails,name='courierdetails'),
    path('financeoffice/<int:deliveryorderid>/',views.invoiceDetails,name='invoicedetails'),
    path('approveInvoiceList/<int:deliveryorderid>/',views.approveInvoice,name='approveInvoicedetails'),

    path('create/',views.createDeliveryOrder,name='createDeliveryOrder'),
    path('<int:deliveryorderid>/',views.details,name='details'),

    path('',views.index,name='index'),

    path('approveDOList/',views.approveDeliveryOrderList,name='approveDOlist'),
    path('approveInvoiceList/',views.approveInvoiceList,name='approveInvoiceList'),

    path('courierList/',views.courierDeliveryOrderList,name='courierList'),
    path('financeoffice/',views.financeDeliveryOrderList,name='financeList'),
    path('invoiceList/',views.invoiceList,name='invoiceList'),
    

]