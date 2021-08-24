from django.forms import ModelForm
from django import forms
from .models import Post 
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

    
    
    
