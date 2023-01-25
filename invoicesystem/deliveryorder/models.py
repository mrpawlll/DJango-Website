from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone



# Create your models here.
class Item(models.Model):
    itemID = models.AutoField(unique=True,primary_key=True)
    itemPrice = models.DecimalField(default=0,max_digits=19,decimal_places=2)
    itemDescription = models.CharField(max_length=30)
    def __str__(self):
        string = str("{:04d}".format(self.itemID))
        return string

    def item_price(self):
        string = 'RM'+ str(self.itemPrice)
        return string
    
    def item_id(self):
        string = str("{:04d}".format(self.itemID))
        return string

    def save(self):
        self.itemDescription = self.itemDescription.upper()
        super().save()

#deliveryorder status
class Status(models.IntegerChoices):
    pending = 1
    disapproved = 2
    approved = 3

class DeliveryOrderForm(models.Model):
    deliveryOrderID = models.AutoField(unique=True,primary_key=True)
    vendorName = models.CharField(max_length=30)
    vendorAddress = models.CharField(max_length=200)
    recipientName = models.CharField(max_length=30)
    recipientPhone = PhoneNumberField(blank=False)
    recipientAddress = models.CharField(max_length=200)
    deliveryOrderStatus = models.IntegerField(default=Status.pending,choices=Status.choices)
    deliveryOrderDate = models.DateTimeField(default=timezone.now)

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
    
    # class Meta:
    #     permissions = [
    #         (
    #             "add_deliveryorderform",
    #             "Can add delivery order form"
    #             ), 
    #         (
    #             "change_deliveryorderform",
    #             "Can change delivery order form"
    #             ), 
    #         (
    #             "delete_deliveryorderform",
    #             "Can delete delivery order form"
    #             ),
    #         (
    #             "view_deliveryorderform",
    #             "Can view delivery order form"
    #             ),
    #     ]
        
    
    def save(self):
        self.vendorName = self.vendorName.upper()
        self.vendorAddress = self.vendorAddress.upper()
        self.recipientName = self.recipientName.upper()
        self.recipientAddress = self.recipientAddress.upper()
        super().save()

class TableList(models.Model):
    deliveryOrderID = models.ForeignKey(DeliveryOrderForm,on_delete = models.CASCADE)
    itemID = models.ForeignKey(Item,on_delete=models.PROTECT)
    itemQuantity = models.IntegerField(default=0)

    def __str__(self):
        string = str(self.deliveryOrderID)+' '+str(self.itemID) + '-'+ str(self.itemQuantity)
        return string
    
    def item_ID(self):
        return self.itemID

    def item_description(self):
        return self.itemID.itemDescription



