from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Item(models.Model):
    itemID = models.AutoField(unique=True,primary_key=True)
    itemPrice = models.IntegerField
    itemDescription = models.CharField(max_length=30)

    def __str__(self):
        return self.itemDescription

    def item_price(self):
        return self.itemPrice

class DeliveryOrder(models.Model):
    deliveryOrderID = models.AutoField(unique=True,primary_key=True)
    vendorName = models.CharField(max_length=30)
    vendorAddress = models.CharField(max_length=200)
    recipientName = models.CharField(max_length=30)
    recipientPhone = PhoneNumberField(blank=False)
    recipientAddress = models.CharField(max_length=200)
    deliveryOrderStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.vendorName + ' ' + self.deliveryOrderID
    

