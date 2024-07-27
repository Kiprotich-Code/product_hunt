from django import forms
from lead.models import Product, Contact

# create forms 
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'