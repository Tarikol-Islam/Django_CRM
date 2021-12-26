from typing import List
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Order,Company,Product
from django.urls import reverse_lazy


# Create your views here.
class OrderListView(ListView):
    model = Order
    #context_object_name = "I can chose any name isntead of "object_list""
    template_name = 'sales/orders.html'


class CompanyListView(ListView):
    model = Company
    template_name = 'sales/company.html'

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company_list')
    template_name = 'sales/companycreate.html'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company_list')
    template_name = 'sales/companyupdate.html'

class CompanyDeleteView(DeleteView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company_list')
    template_name = 'sales/companydelete.html'






#Product View part
class ProductListView(ListView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'sales/products.html'

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    template_name = 'sales/productscreate.html'

class ProductUpdateView(UpdateView):    
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    template_name = 'sales/productsupdate.html'

class ProductDeleteView(DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    template_name = 'sales/productsdelete.html'


