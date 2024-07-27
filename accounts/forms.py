from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Row, Column

# Create your forms here 
class MemberRegisterForm(UserCreationForm):
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Enter Password'}
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Confirm Password'}
    ))

    class Meta():
        model = CustomUser
        fields = ['email', 'full_names', 'password', 'password2', ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': "Member's Email Address"}),
            'full_names': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': "Member's Name"}),
        }


class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder' :'Email', 'style': 'max-width: 600px;'}))
    password = forms.CharField(
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

    class Meta:
        model = CustomUser
        fields = ('email', 'password', )



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dp', 'club_role', 'bio', 'designation', ]

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('dp', 'club_role', 'designation', css_class='col-md-4'),
                Column('bio', css_class='col-md-8'),
            ),
            Submit('submit', u'Update Profile', css_class='btn btn-primary mb-3'),
        )  
