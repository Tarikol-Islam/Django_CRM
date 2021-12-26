from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

from .models import RawMaterial, RawOrder, Supplier

# Create your views here.
# listViews
class RawMaterialListView(ListView):
    model = RawMaterial
    template_name = 'production/rawmaterials.html'

class SupplierListView(ListView):
    model = Supplier
    template_name = 'production/suppliers.html'

class RawOrderListView(ListView):
    model = RawOrder
    template_name = 'production/raworders.html'

#####CreateViews

class RawMaterialListView(CreateView):
    model = RawMaterial
    template_name = 'production/rawmaterialscreate.html'

class SupplierListView(CreateView):
    model = Supplier
    template_name = 'production/supplierscreate.html'

class RawOrderListView(CreateView):
    model = RawOrder
    template_name = 'production/raworderscreate.html'


#####updateviews

class RawMaterialListView(UpdateView):
    model = RawMaterial
    template_name = 'production/rawmaterialsupdate.html'

class SupplierListView(UpdateView):
    model = Supplier
    template_name = 'production/suppliersupdate.html'

class RawOrderListView(UpdateView):
    model = RawOrder
    template_name = 'production/rawordersupdate.html'


#####deleteviews

class RawMaterialListView(DeleteView):
    model = RawMaterial
    template_name = 'production/rawmaterialsdelete.html'

class SupplierListView(DeleteView):
    model = Supplier
    template_name = 'production/suppliersdelete.html'

class RawOrderListView(DeleteView):
    model = RawOrder
    template_name = 'production/rawordersdelete.html'
