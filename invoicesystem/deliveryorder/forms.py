from django.forms import forms,ModelForm,inlineformset_factory
from .models import DeliveryOrderForm


# class DOForm(ModelForm):
#     class Meta:
#         model = DeliveryOrderForm
#         fields = '__all__'



     
class DOForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'deliveryOrderID',
    'recipientName',
    'recipientPhone',
    'recipientAddress',
    'deliveryOrderDate',
    'itemID',
    'itemPrice',
    'itemDescription',
    'itemQuantity',]

class approveDOForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientName',
    'recipientPhone',
    'recipientAddress',
    'deliveryOrderDate',
    'itemID',
    'itemPrice',
    'itemDescription',
    'itemQuantity',
    'deliveryOrderStatus']

class courierForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientName',
    'recipientPhone',
    'recipientAddress',
    'deliveryOrderDate',
    'itemID',
    'itemPrice',
    'itemDescription',
    'itemQuantity',
    'courierStatus']

class invoiceForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientName',
    'recipientPhone',
    'recipientAddress',
    'deliveryOrderDate',
    'itemID',
    'itemPrice',
    'itemDescription',
    'itemQuantity',
    'invoiceTotal',
    'invoiceCreated']

class approveInvoiceForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientName',
    'recipientPhone',
    'recipientAddress',
    'deliveryOrderDate',
    'itemID',
    'itemPrice',
    'itemDescription',
    'itemQuantity',
    'invoiceTotal',
    'invoiceStatus']

