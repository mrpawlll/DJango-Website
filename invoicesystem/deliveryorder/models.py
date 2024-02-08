from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


#deliveryorder status
class Status(models.IntegerChoices):
    pending = 1
    disapproved = 2
    approved = 3

class DeliveryOrderForm(models.Model):
    deliveryorderid = models.AutoField(unique=True,primary_key=True)
    vendorname = models.CharField(default = 'AGIS', max_length=30)
    vendoraddress = models.CharField(default = 'Cyberjaya' ,max_length=200)
    recipientname = models.CharField(default = 'recipientName',max_length=30)
    recipientphone = PhoneNumberField(blank=False)
    recipientaddress = models.CharField(default = 'recipientaddress',max_length=200)
    deliveryorderdate = models.DateTimeField(default=timezone.now)

    deliveryorderstatus = models.IntegerField(default=Status.pending,choices=Status.choices)
    courierstatus = models.IntegerField(default = Status.pending,choices=Status.choices)
    invoicestatus = models.IntegerField(default = Status.pending,choices=Status.choices)
    invoicecreated = models.BooleanField(default=False)

    itemid = models.IntegerField(default = 0)
    itemprice = models.DecimalField(default=0,max_digits=19,decimal_places=2)
    itemdescription = models.CharField(default = 'empty',max_length=30)
    itemquantity = models.IntegerField(default=0)
    invoicetotal = models.DecimalField(default=0,max_digits=19,decimal_places=2)

    def __str__(self):
        string = 'ID : ' + str(self.deliveryorderid) + ' - ' + self.recipientname
        return string

    def id(self):
        string = str("{:04d}".format(self.deliveryorderid))
        return string

    def nextid(self):
        string = str("{:04d}".format(self.deliveryorderid+1))
        return string
    
    def date(self):
        date = self.deliveryorderdate.date()
        return date.strftime("%B %d %Y")    

    def vendor_name(self):
        return self.vendorName
    
    def status(self):
        status = self.deliveryorderstatus
        if status == 3:
            status = "Approved"
        elif status == 2:
            status = "Disapproved"
        else:
            status = "Pending"
        return status
    
    def courierStat(self):
        courierStat = self.courierstatus
        if courierStat == 3:
            courierStat = "Approved"
        elif courierStat == 2:
            courierStat = "Disapproved"
        else:
            courierStat = "Pending"
        return courierStat
    
    @property
    def invoiceStat(self):
        if self.invoicestatus == 3:
            return "Approved"
        elif self.invoicestatus == 2:
            return "Disapproved"
        else:
            return "Pending"
        
    def save(self):
        self.vendorname = self.vendorname.upper()
        self.vendoraddress = self.vendoraddress.upper()
        self.recipientname = self.recipientname.upper()
        self.recipientaddress = self.recipientaddress.upper()
        self.invoicetotal= self.itemquantity *  self.itemprice
        super().save()





