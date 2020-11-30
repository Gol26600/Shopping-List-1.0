from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Add new product...',
                'size': 39,
                'style': 'height:45px'}),
            'quantity': forms.TextInput(attrs={
                'placeholder': 'Num',
                'size': 5,
                'style': 'height:45px'}),
            'unit': forms.Select(attrs={
                'style': 'height:45px'})
        }


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(attrs={
                'placeholder': 'Type in your notes...',
                'cols': 59})
        }
