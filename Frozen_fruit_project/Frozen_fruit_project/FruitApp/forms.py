from django import  forms
from .models import *

class OrderForm(forms.models.ModelForm):
    class Meta:
        model = Order
        fields = ['fruit','customer_name','contact','quantity_ordered']