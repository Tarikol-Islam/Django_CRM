from django import forms
from .models import Supplier,RawOrder,RawMaterial

class SupplierForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = ("",)


class RawOrderForm(forms.ModelForm):
    
    class Meta:
        model = RawOrder
        fields = ("",)



class RawMaterailForm(forms.ModelForm):
    
    class Meta:
        model = RawMaterial
        fields = ("",)