from django import forms
from .models import *

class FilterForm(forms.Form):
    date_from = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    date_to = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
    record_type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(), required=False)


