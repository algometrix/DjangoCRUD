from django import forms

class FooForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())

class BarForm(forms.Form):
    fooid = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
 