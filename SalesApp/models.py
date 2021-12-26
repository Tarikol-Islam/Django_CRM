from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 30, null=True)
    product_price = models.FloatField(default = 0, null=True)
    product_desc = models.CharField(max_length = 300, null=True)
    product_qty = models.IntegerField(default = 1, null=True)
    product_pic = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return self.product_name

class Company(models.Model):
    business_name = models.CharField(max_length = 30, null=False)
    business_address = models.CharField(max_length= 300, null=False)
    business_product = models.TextField()
    business_bank_account = models.CharField(max_length=30,null=True)
    business_website = models.URLField(default="www."+".bd.com",null=True)
    business_email = models.EmailField(null = True, default=business_name)
    business_contact_number = models.CharField(max_length=14,null=True)
    business_contact_person = models.CharField(max_length=80,null=False)
    business_status = models.CharField(max_length=50,null=False, default="National")
    
    def __str__(self):
        return self.business_name


class Order(models.Model):
    order_name = models.CharField(max_length = 30, null=True)
    order_items = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_qty = models.IntegerField(default=1, null=True)
    order_details = models.TextField()
    payment_status = models.BooleanField(default=False)
    customer_details = models.ForeignKey(Company,models.CASCADE)
    order_total_price = models.FloatField(null=True)
    order_date = models.DateField(default= timezone.now)
    delivery_date = models.DateField(default= timezone.now)
    
    def __str__(self):
        return self.order_name



