from django import forms

class FooForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    bar_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Optional'}),required=False)

class BarForm(forms.Form):
    foo_id = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())