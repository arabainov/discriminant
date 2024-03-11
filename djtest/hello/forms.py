from django import forms

class SquareForm(forms.Form):
    a = forms.FloatField(label="a")
    b = forms.FloatField(label="b")
    c = forms.FloatField(label="c")

class ProbabilityForm(forms.Form):
    k = forms.IntegerField(label="k")
    n = forms.IntegerField(label="n")
    p = forms.FloatField(label="p")