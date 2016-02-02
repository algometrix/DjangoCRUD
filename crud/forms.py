from django import forms

class FooForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())

class BarForm(forms.Form):
    fooid = forms.IntegerField(widget=forms.TextInput(attrs={'type':'number'}))
    name = forms.CharField(widget=forms.TextInput())
 