from django.forms import forms,ModelForm,inlineformset_factory
from .models import DeliveryOrderForm,TableList


class DOForm(ModelForm):
    class Meta:
        model = DeliveryOrderForm
        fields = '__all__'


