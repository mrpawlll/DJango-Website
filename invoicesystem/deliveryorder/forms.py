from django.forms import forms,ModelForm
from .models import DeliveryOrderForm

class DOForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = '__all__'


