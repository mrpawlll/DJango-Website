from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Item,DeliveryOrderForm, TableList
# Register your models here.

class TableListInline(admin.TabularInline):
    model = TableList
    extra = 3

class DeliveryOrderAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Delivery Order Details', {'fields' :['vendorName','vendorAddress','recipientName','recipientAddress','recipientPhone','deliveryOrderDate','deliveryOrderStatus'] })
    ]
    inlines = [TableListInline]


admin.site.register(Item)
admin.site.register(DeliveryOrderForm,DeliveryOrderAdmin)
admin.site.register(Permission)