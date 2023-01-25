from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.db.models import F
from django.views import generic
from django.forms import inlineformset_factory,modelformset_factory
from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required, permission_required

from .models import DeliveryOrderForm, TableList, Item
from .forms import DOForm
# Create your views here.
@login_required
@permission_required('deliveryorder.view_deliveryorderform',raise_exception=True)
# @permission_required('deliveryorder.view_deliveryorderform',login_url=reverse_lazy('login:login'))
def index(request):

    deliveryOrderList = get_list_or_404(DeliveryOrderForm.objects.filter())

    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/index.html',context)

def details(request,deliveryOrderID):
    deliveryOrderID = get_object_or_404(DeliveryOrderForm,pk = deliveryOrderID)
    return render(request,'deliveryorder/details.html',{'deliveryOrderID':deliveryOrderID})

def createDeliveryOrder(request):
    model = DeliveryOrderForm
    template_name = 'deliveryorder/create.html'
    deliveryOrderID = get_object_or_404(
        DeliveryOrderForm.objects.order_by('-deliveryOrderID')[:1]
    )

    form = inlineformset_factory(DeliveryOrderForm,TableList, fields = [
    'deliveryOrderID',
    'vendorName',
    'vendorAddress',
    'recipientName',
    'recipientPhone',
    'recipientAddress',
    'deliveryOrderStatus',
    'deliveryOrderDate',
    'itemID',
    'itemQuantity',
    ])

    if form.is_valid():
        form.save()
        return redirect_lazy('deliveryorder:index')

    context = {
        'deliveryOrderID':deliveryOrderID,
        'form':form
    }
    return render(request,template_name,context)

