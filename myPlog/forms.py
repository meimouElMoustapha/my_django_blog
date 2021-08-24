from django.forms import ModelForm
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Reordering Form and View


# class PositionForm(forms.ModelForm):
#     position = forms.CharField()
    
class Postnote(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=['title','field','content','comment','Image']
        
        widgets={
           
            'title': forms.TextInput(attrs={'class':'form-control'}),
             'field': forms.TextInput(attrs={'class':'form-control' } ),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'comment': forms.TextInput(attrs={'class':'form-control'}),
           
            
        }
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
       
       