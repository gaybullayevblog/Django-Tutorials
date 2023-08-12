from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    # age = forms.IntegerField(label="Age")
    # position = forms.CharField(label="Position", max_length=255)
    # email = forms.EmailField(label="Email", max_length=100)

