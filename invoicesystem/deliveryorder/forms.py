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
    'recipientName',
    'recipientPhone',
    'recipientAddress',
    'deliveryOrderDate',
    'itemID',
    'itemPrice',
    'itemDescription',
    'itemQuantity',]
