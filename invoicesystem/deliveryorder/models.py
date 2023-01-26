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
    deliveryOrderDate = models.DateTimeField(default=timezone.now)

    deliveryOrderStatus = models.IntegerField(default=Status.pending,choices=Status.choices)
    courierStatus = models.IntegerField(default = Status.pending,choices=Status.choices)
    invoiceStatus = models.IntegerField(default = Status.pending,choices=Status.choices)
    invoiceCreated = models.BooleanField(default=False)

    itemID = models.IntegerField(default = 0)
    itemPrice = models.DecimalField(default=0,max_digits=19,decimal_places=2)
    itemDescription = models.CharField(default = 'empty',max_length=30)
    itemQuantity = models.IntegerField(default=0)
    invoiceTotal = models.DecimalField(default=0,max_digits=19,decimal_places=2)

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
    
    def courierStat(self):
        courierStat = self.courierStatus
        if courierStat == 3:
            courierStat = "Approved"
        elif courierStat == 2:
            courierStat = "Disapproved"
        else:
            courierStat = "Pending"
        return courierStat
    
    def invoiceStat(self):
        invoiceStat = self.invoiceStatus
        if invoiceStat == 3:
            invoiceStat = "Approved"
        elif invoiceStat == 2:
            invoiceStat = "Disapproved"
        else:
            invoiceStat = "Pending"
        return invoiceStat
        
    def save(self):
        self.vendorName = self.vendorName.upper()
        self.vendorAddress = self.vendorAddress.upper()
        self.recipientName = self.recipientName.upper()
        self.recipientAddress = self.recipientAddress.upper()
        self.invoiceTotal= self.itemQuantity *  self.itemPrice
        super().save()





