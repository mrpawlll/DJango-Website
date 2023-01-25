from http.client import HTTPResponse
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.forms import inlineformset_factory,modelformset_factory

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

def createDeliveryOrder(request,id=None):
    model = DeliveryOrderForm

    # temp = get_object_or_404(model.objects.get(pk=id))
    # qs = temp.TableList_set.all()
    template_name = 'deliveryorder/create.html'
    deliveryOrderID = get_object_or_404(
        model.objects.order_by('-deliveryOrderID')[:1]
    )

    initialformset = inlineformset_factory(DeliveryOrderForm,TableList, fields = [
    'itemID',
    'itemQuantity',
    ])


    if request.method == 'POST':
        form = DOForm(request.POST)
        if form.is_valid() and formset.is_valid():
            form.save(commit = False)
            formset.save(commit = False)
            print("form",form.cleaned_data)
            print("formset",formset.cleaned_data)
            return HttpResponseRedirect('thanks/')
   
    else: 
        if request.method == 'GET':
            form = DOForm()
            formset = initialformset()

    context = {
        'deliveryOrderID':deliveryOrderID,
        'form':form,
        'formset':formset
    }
    return render(request,template_name,context)

