

from django import forms

class AddElement(forms.Form):
    
   title = forms.CharField(max_length=100, label='Title', required=True)
   size = forms.CharField(max_length=100, label='size', required=True)
   Producer_Name = forms.CharField(max_length=100, label='Producer_Name', required=True)
   price = forms.CharField(required=True, label='price')
   color = forms.CharField(required=True, label='color')
   structure = forms.CharField(required=True, label='structure')
   image = forms.ImageField(label='Image')

