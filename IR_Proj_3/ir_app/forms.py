from django import forms
from Assignment_4_App.models import Product_Inv

class Product_Inv_Forms(forms.ModelForm):
    class Meta:
        model = Product_Inv
        fields = "__all__"