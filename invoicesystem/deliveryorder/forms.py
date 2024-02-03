from django.forms import ModelForm
from .models import DeliveryOrderForm


# class DOForm(ModelForm):
#     class Meta:
#         model = DeliveryOrderForm
#         fields = '__all__'



     
class DOForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'deliveryorderid',
    'recipientname',
    'recipientphone',
    'recipientaddress',
    'deliveryorderdate',
    'itemid',
    'itemprice',
    'itemdescription',
    'itemquantity',]

class approveDOForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientname',
    'recipientphone',
    'recipientaddress',
    'deliveryorderdate',
    'itemid',
    'itemprice',
    'itemdescription',
    'itemquantity',
    'deliveryorderstatus']

class courierForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'deliveryorderid',
    'recipientname',
    'recipientphone',
    'recipientaddress',
    'deliveryorderdate',
    'itemid',
    'itemprice',
    'itemdescription',
    'itemquantity',
    'courierstatus']

class invoiceForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientname',
    'recipientphone',
    'recipientaddress',
    'deliveryorderdate',
    'itemid',
    'itemprice',
    'itemdescription',
    'itemquantity',
    'invoicetotal',
    'invoicecreated']

class approveInvoiceForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientname',
    'recipientphone',
    'recipientaddress',
    'deliveryorderdate',
    'itemid',
    'itemprice',
    'itemdescription',
    'itemquantity',
    'invoicetotal',
    'invoicestatus']

