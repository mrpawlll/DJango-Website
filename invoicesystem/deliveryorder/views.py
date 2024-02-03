from http.client import HTTPResponse
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404,redirect
from django.urls import reverse_lazy
from django.forms import inlineformset_factory,modelformset_factory
from django.db.models import Q


from django.contrib.auth.decorators import login_required, permission_required

from .models import DeliveryOrderForm
from .forms import DOForm, approveDOForm, courierForm,invoiceForm, approveInvoiceForm
# Create your views here.
@login_required
@permission_required('deliveryorder.view_deliveryorderform',raise_exception=True)
def index(request):

    deliveryOrderList = list(DeliveryOrderForm.objects.filter())

    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/index.html',context)

@login_required
def details(request,deliveryorderid):
    deliveryorder = get_object_or_404(DeliveryOrderForm,pk=deliveryorderid)
    return render(request,'deliveryorder/details.html',{'deliveryorder':deliveryorder})

@login_required
def createDeliveryOrder(request):
    submitted = False
    deliveryorderid = DeliveryOrderForm.objects.order_by('-deliveryorderid')[:1]
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
            'deliveryOrderID':deliveryorderid,
            'form':form
        }

    return render(request,template_name,context)




#manager
@login_required
@permission_required('deliveryorder.view_deliveryorderform',raise_exception=True)
def approveDeliveryOrderList(request):

    deliveryOrderList = list(DeliveryOrderForm.objects.filter(deliveryorderstatus=1))

    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/index.html',context)

@login_required
def approveDetails(request,deliveryorderid):
    submitted = False
    template_name = 'deliveryorder/approvedeliveryorder.html'

    delivery = DeliveryOrderForm.objects.get(pk=deliveryorderid)

    form = approveDOForm(instance=delivery)
    if request.method == 'POST':
        form = approveDOForm(request.POST,instance=delivery)
        if form.is_valid():
            form.save()
            submitted = True
            return redirect("deliveryorder:approveDOlist")
        else:
            print(form.errors)

    context= {
            'submitted':submitted,
            'form':form,
            'deliveryorderid':delivery
        }

    return render(request,template_name,context)


@login_required
def approveInvoiceList(request):

    deliveryOrderList = list(DeliveryOrderForm.objects.filter(invoicestatus=1,invoicecreated=True))

    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/indexinvoice.html',context)

@login_required
def approveInvoice(request,deliveryorderid):
    submitted = False
    template_name = 'deliveryorder/approveinvoice.html'

    delivery = DeliveryOrderForm.objects.get(pk=deliveryorderid)

    form = approveInvoiceForm(instance=delivery)
    if request.method == 'POST':
        form = approveInvoiceForm(request.POST,instance=delivery)
        if form.is_valid():
            form.save()
            submitted = True
            return redirect("deliveryorder:approveInvoiceList")
        else:
            print(form.errors)

    context= {
            'submitted':submitted,
            'form':form,
            'deliveryOrderID':delivery
        }

    return render(request,template_name,context)





#courier
@login_required
@permission_required('deliveryorder.view_deliveryorderform',raise_exception=True)
def courierDeliveryOrderList(request):

    deliveryOrderList = list(DeliveryOrderForm.objects.filter(deliveryorderstatus=3))
    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/index.html',context)

@login_required
def courierDetails(request,deliveryorderid):
    submitted = False
    template_name = 'deliveryorder/updateCourierDeliveryOrder.html'

    delivery = DeliveryOrderForm.objects.get(pk=deliveryorderid)

    form = courierForm(instance=delivery)
    if request.method == 'POST':
        form = courierForm(request.POST,instance=delivery)
        if form.is_valid():
            form.save()
            submitted = True
            return redirect("deliveryorder:courierList")
        else:
            print(form.errors)

    context= {
            'submitted':submitted,
            'form':form
        }

    return render(request,template_name,context)




#finance office
@login_required
@permission_required('deliveryorder.view_deliveryorderform',raise_exception=True)
    #courier approved
def financeDeliveryOrderList(request):
    deliveryOrderList = list(DeliveryOrderForm.objects.filter(courierstatus=3,invoicecreated=False))
    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/index.html',context)

@login_required
    #created invoice
def invoiceList(request):
    deliveryOrderList = list(DeliveryOrderForm.objects.filter(courierstatus=3,invoicecreated=True))
    context = {
    'deliveryOrderList' : deliveryOrderList
    }
    return render(request,'deliveryorder/indexinvoice.html',context)

@login_required
def invoiceDetails(request,deliveryorderid):
    submitted = False
    template_name = 'deliveryorder/invoice.html'

    delivery = DeliveryOrderForm.objects.get(pk=deliveryorderid)

    form = invoiceForm(instance=delivery)


    if request.method == 'POST':
        form = invoiceForm(request.POST,instance=delivery)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.invoicecreated = True
            obj.invoicestatus = 1
            obj.save()
            submitted = True
            return redirect("deliveryorder:financeList")
        else:
            print(form.errors)

    context= {
            'submitted':submitted,
            'form':form,
            'deliveryOrderID': delivery
        }

    return render(request,template_name,context)

