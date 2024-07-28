from django import forms
from lead.models import Product, Contact

# create forms 
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'sub_title', 'desc', 'category', )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'