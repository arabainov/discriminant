from django import forms

class SquareForm(forms.Form):
    a = forms.FloatField(label="a")
    b = forms.FloatField(label="b")
    c = forms.FloatField(label="c")

class ProbabilityForm(forms.Form):
    a = forms.IntegerField(label="k")
    b = forms.IntegerField(label="n")
    c = forms.IntegerField(label="p")