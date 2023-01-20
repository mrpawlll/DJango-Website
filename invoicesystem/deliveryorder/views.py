from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.db.models import F
from django.views import generic

from django.contrib.auth.decorators import login_required, permission_required

from .models import DeliveryOrderForm, TableList

# Create your views here.
@login_required
# @permission_required('deliveryorder.view_deliveryorderform',raise_exception=True)
@permission_required('deliveryorder.view_deliveryorderform',login_url=reverse_lazy('login:login'))
def index(request):

    deliveryOrderList = get_list_or_404(DeliveryOrderForm.objects.filter())

    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/index.html',context)

def details(request,deliveryOrderID):
    deliveryOrderID = get_object_or_404(DeliveryOrderForm,pk = deliveryOrderID)
    return render(request,'deliveryorder/details.html',{'deliveryOrderID':deliveryOrderID})

