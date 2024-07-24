from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Create your forms here 
class MemberRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Enter Password'}
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Confirm Password'}
    ))

    class Meta():
        model = CustomUser
        fields = ['email', 'full_names', 'password1', 'password2', ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': "Member's Email Address"}),
            'full_names': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': "Member's Name"}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder' :'Email', 'style': 'max-width: 600px;'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'style': 'max-width: 600px;'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
                'style': 'max-width: 600px;'
            }
        )
    )