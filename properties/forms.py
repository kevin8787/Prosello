from django import forms
from django.core.exceptions import ValidationError

from properties.models import Property


class PropertyForm(forms.ModelForm):
    print("-----------------------")
    property_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'Enter Property name'}),
                                                        error_messages={'required': 'Please Enter Property Name'})
    property_desc = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'Enter Property descripion'}),
                                                        error_messages={'required': 'Please Enter Property description'})
    property_city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'Enter Property city'}),
                                                         error_messages={'required': 'Please Enter Property city'})
    property_address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'Enter Property address'}),
                                                        error_messages={'required': 'Please Enter Property address'})
    property_price = forms.DecimalField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'Enter Property price'}),
                                                        error_messages={'required': 'Please Enter Property price'})
    property_owner = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': "Enter Property owner's name"}),
                                                        error_messages={'required': 'Please Enter Property owner name'})
    property_contact = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'Enter Property contact Number'}),
                                                        error_messages={'required': 'Please Enter Property contact number'})
    # property_image = forms.ImageField(required=False)                                       

    class Meta:
        model = Property
        fields = ["property_name","property_desc","property_city","property_address","property_price","property_owner","property_contact"]
    
