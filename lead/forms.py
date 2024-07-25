from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser
from .models import Category, Product

# CREATE YOUR FORMS HERE 
class AddUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_names', 'user_type', )


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_names', 'user_type', )


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
