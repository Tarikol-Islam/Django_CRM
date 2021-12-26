from typing import Pattern
from django.urls import path
from .views import *

urlpatterns = [
    path('order/',OrderListView.as_view(), name = 'orders_list'),
    #Company Part
    path('company/',CompanyListView.as_view(), name = 'company_list'),
    path('company/create/',CompanyCreateView.as_view(), name = 'create_company'),
    path('company/<int:pk>/update/',CompanyUpdateView.as_view(), name = 'update_company'),
    path('company/<int:pk>/delete/',CompanyDeleteView.as_view(), name = 'delete_company'),
    #Product Part
    path('product/',ProductListView.as_view(), name = 'product_list'),
    path('product/create/',ProductCreateView.as_view(), name = 'create_product'),
    path('product/<int:pk>/update/',ProductUpdateView.as_view(), name = 'update_product'),
    path('product/<int:pk>/delete/',ProductDeleteView.as_view(), name = 'delete_product'),
]
