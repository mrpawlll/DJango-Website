from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import DeliveryOrderForm
# Register your models here.


class DeliveryOrderAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Delivery Order Details', 
        {'fields' :[
            'vendorName',
            'vendorAddress',
            'recipientName',
            'recipientAddress',
            'recipientPhone',
            'deliveryOrderDate',
            'deliveryOrderStatus',
            'itemID',
            'itemPrice',
            'itemDescription',
            'itemQuantity',]
        }
            )]

admin.site.register(DeliveryOrderForm,DeliveryOrderAdmin)
admin.site.register(Permission)