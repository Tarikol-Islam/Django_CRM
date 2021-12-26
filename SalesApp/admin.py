from django.contrib import admin

from SalesApp.models import Company, Order, Product

# Register your models here.
admin.site.register(Company)
admin.site.register(Order)
admin.site.register(Product)