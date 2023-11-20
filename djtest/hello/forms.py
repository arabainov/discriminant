from django import forms

class NumbersForm(forms.Form):
    a = forms.FloatField(label="a")
    b = forms.FloatField(label="b")
    c = forms.FloatField(label="c")

