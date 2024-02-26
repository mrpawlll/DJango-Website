from django.forms import ModelForm
from .models import DeliveryOrderForm


# class DOForm(ModelForm):
#     class Meta:
#         model = DeliveryOrderForm
#         fields = '__all__'



     
class DOForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DOForm, self).__init__(*args, **kwargs)
        self.fields['deliveryorderdate'].widget.attrs['readonly'] = True

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
    def __init__(self, *args, **kwargs):    
        super(approveDOForm, self).__init__(*args, **kwargs)
        # set every field to be readonly, but deliveryorderstatus field is not set as readonly due to it's value not being set before this
        # you can view the def approveDetails() where we populate this form with form = approveDOForm(instance=delivery), which is taking data only when
        # salesman first create the form. salesman did not select anything for deliveryorderstatus, thus this value is editable although
        # in our __init__ we set every self.fields.values to be readonly
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

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
    def __init__(self, *args, **kwargs):    
        super(courierForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

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
    def __init__(self, *args, **kwargs):    
        super(invoiceForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

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
    def __init__(self, *args, **kwargs):    
        super(approveInvoiceForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

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

