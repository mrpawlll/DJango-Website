from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


#deliveryorder status
class Status(models.IntegerChoices):
    pending = 1
    disapproved = 2
    approved = 3

class DeliveryOrderForm(models.Model):
    deliveryOrderID = models.AutoField(unique=True,primary_key=True)
    vendorName = models.CharField(default = 'vendorname', max_length=30)
    vendorAddress = models.CharField(default = 'Cyberjaya' ,max_length=200)
    recipientName = models.CharField(default = 'recipientName',max_length=30)
    recipientPhone = PhoneNumberField(blank=False)
    recipientAddress = models.CharField(default = 'recipientaddress',max_length=200)
    deliveryOrderStatus = models.IntegerField(default=Status.pending,choices=Status.choices)
    deliveryOrderDate = models.DateTimeField(default=timezone.now)

    itemID = models.IntegerField(default = 0)
    itemPrice = models.DecimalField(default=0,max_digits=19,decimal_places=2)
    itemDescription = models.CharField(default = 'empty',max_length=30)
    itemQuantity = models.IntegerField(default=0)

    def __str__(self):
        string = 'ID : ' + str(self.deliveryOrderID) + ' - ' + self.recipientName
        return string

    def id(self):
        string = str("{:04d}".format(self.deliveryOrderID))
        return string

    def nextid(self):
        string = str("{:04d}".format(self.deliveryOrderID+1))
        return string
    
    def date(self):
        date = self.deliveryOrderDate.date()
        return date.strftime("%B %d %Y")    

    def vendor_name(self):
        return self.vendorName
    
    def status(self):
        status = self.deliveryOrderStatus
        if status == 3:
            status = "Approved"
        elif status == 2:
            status = "Disapproved"
        else:
            status = "Pending"
        return status
    
        
    def save(self):
        self.vendorName = self.vendorName.upper()
        self.vendorAddress = self.vendorAddress.upper()
        self.recipientName = self.recipientName.upper()
        self.recipientAddress = self.recipientAddress.upper()
        super().save()





