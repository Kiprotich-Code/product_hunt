from django import forms
from lead.models import Product

# create forms 
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'