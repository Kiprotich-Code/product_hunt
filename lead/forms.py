from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

# CREATE YOUR FORMS HERE 
class AddUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'