from http.client import HTTPResponse
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404,redirect
from django.urls import reverse_lazy
from django.forms import inlineformset_factory,modelformset_factory

from django.contrib.auth.decorators import login_required, permission_required

from .models import DeliveryOrderForm
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
    submitted = False
    model = DeliveryOrderForm
    deliveryOrderID = get_object_or_404(model.objects.order_by('-deliveryOrderID')[:1])
    template_name = 'deliveryorder/create.html'

    form = DOForm()
    if request.method == 'POST':
        form = DOForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            return redirect("deliveryorder:index")
        else:
            print(form.errors)

    context= {
            'submitted':submitted,
            'deliveryOrderID':deliveryOrderID,
            'form':form
        }

    return render(request,template_name,context)

@login_required
@permission_required('deliveryorder.view_deliveryorderform',raise_exception=True)
def approveDeliveryOrderList(request):

    deliveryOrderList = get_list_or_404(DeliveryOrderForm.objects.filter(status='Pending'))

    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/index.html',context)


