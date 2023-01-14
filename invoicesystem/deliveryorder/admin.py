from django.contrib import admin

from .models import Item,DeliveryOrderForm, TableList
# Register your models here.

class TableListInline(admin.TabularInline):
    model = TableList
    extra = 3

class DeliveryOrderAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Delivery Order Details', {'fields' :['vendorName','vendorAddress','recipientName','recipientAddress','recipientPhone'] })
    ]
    inlines = [TableListInline]


admin.site.register(Item)
admin.site.register(DeliveryOrderForm,DeliveryOrderAdmin)