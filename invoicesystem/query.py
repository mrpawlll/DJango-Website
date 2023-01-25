import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoicesystem.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, get_object_or_404

from deliveryorder.models import DeliveryOrderForm
from deliveryorder.forms import DOForm

def run():
    deliveryOrderID = get_object_or_404(
        DeliveryOrderForm.objects.order_by('-deliveryOrderID')[:1]
    )
    form = DOForm(initial={'deliveryOrderID':deliveryOrderID.nextid})
    form['deliveryOrderID'].value()


if __name__ == '__main__':
    run()

