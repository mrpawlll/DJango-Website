from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import DeliveryOrderForm
# Register your models here.


class DeliveryOrderAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Delivery Order Details', 
        {'fields' :[
            'vendorname',
            'vendoraddress',
            'recipientname',
            'recipientaddress',
            'recipientphone',
            'deliveryorderdate',
            'deliveryorderstatus',
            'itemid',
            'itemprice',
            'itemdescription',
            'itemquantity',]
        }
            )]

admin.site.register(DeliveryOrderForm,DeliveryOrderAdmin)
admin.site.register(Permission)