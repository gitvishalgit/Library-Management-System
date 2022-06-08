from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import book

class SignupForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
    'class':'form-control'}))
    
class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['title','author','isbn','category']
        labels = {'title':'Title','author':'Author','isbn':'ISBN','category':'CATEGORY'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'author':forms.TextInput(attrs={'class':'form-control'}),
                 'isbn':forms.NumberInput(attrs={'class':'form-control'}),
                 'author':forms.TextInput(attrs={'class':'form-control'})}


class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}

class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Email'}
        widgets={'password':forms.PasswordInput(attrs={'autocomplete':'current-password',
    'class':'form-control'}),
    'last_login':forms.TextInput(attrs={'class':'form-control'}),
    'is_superuser':forms.CheckboxInput(attrs={'class':'form-check'}),
    'groups':forms.Select(attrs={'class':'form-control'}),
    'user_permissions':forms.Select(attrs={'class':'form-select'}),
    'username':forms.TextInput(attrs={'class':'form-control'}),
    'first_name':forms.TextInput(attrs={'class':'form-control'}),
    'last_name':forms.TextInput(attrs={'class':'form-control'}),
    'email':forms.EmailInput(attrs={'class':'form-control'}),
    'is_staff':forms.CheckboxInput(attrs={'class':'form-check'}),
    'is_active':forms.CheckboxInput(attrs={'class':'form-check'}),
    'date_joined':forms.DateInput(attrs={'class':'form-control'}),

    }