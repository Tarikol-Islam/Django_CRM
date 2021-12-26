from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50,null=False)
    supplier_bio = models.TextField(max_length=500, blank=True)
    supplier_address = models.TextField(max_length=200, blank=True, null=True)
    supplier_contact =models.CharField(max_length=14, blank=True)#phonenumber
    supplier_birthdate= models.DateField(null=True, blank=True)
    supplier_supply = models.TextField()
    supplier_img= models.ImageField(default='avatar.png', upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.supplier_name, self.supplier_supply)

#The materials a company need for
class RawMaterial(models.Model):
    raw_name = models.CharField(max_length=50, null=False)
    raw_description = models.TextField()
    raw_qty = models.IntegerField()

    def __str__(self) -> str:
        return self.raw_name
    

#The Materials that moved/request to sell
class RawOrder(models.Model):
    order_by = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    item_is = models.ForeignKey(RawMaterial,on_delete=models.CASCADE)
    asking_price = models.FloatField()
    order_status = CharField(max_length=10,null = False, default="New")

    def __str__(self) -> str:
        return self.item_is.raw_name
