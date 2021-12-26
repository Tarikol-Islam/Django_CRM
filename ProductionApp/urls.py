from django.urls import path
from .views import RawMaterialListView,RawOrderListView,SupplierListView

urlpatterns = [
    #listview
    path('rawmaterials/',RawMaterialListView.as_view(),name = 'raw_materials_list'),
    path('raworders/',RawOrderListView.as_view(),name = 'raw_orders_list'),
    path('suppliers/',SupplierListView.as_view(),name = 'suppliers_list'),
    #create
    path('rawmaterials/create',RawMaterialListView.as_view(),name = 'raw_materials_create'),
    path('raworders/create',RawOrderListView.as_view(),name = 'raw_orders_create'),
    path('suppliers/create',SupplierListView.as_view(),name = 'suppliers_create'),
    #update
    path('rawmaterials/<int:pk>/update',RawMaterialListView.as_view(),name = 'raw_materials_update'),
    path('raworders/<int:pk>/update',RawOrderListView.as_view(),name = 'raw_orders_update'),
    path('suppliers/<int:pk>/update',SupplierListView.as_view(),name = 'suppliers_update'),
    #delete
    path('rawmaterials/<int:pk>/delete',RawMaterialListView.as_view(),name = 'raw_materials_delete'),
    path('raworders/<int:pk>/delete',RawOrderListView.as_view(),name = 'raw_orders_delete'),
    path('suppliers/<int:pk>/delete',SupplierListView.as_view(),name = 'suppliers_delete'),
]
