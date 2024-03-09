from django import forms

class SquareForm(forms.Form):
    a = forms.FloatField(label="a")
    b = forms.FloatField(label="b")
    c = forms.FloatField(label="c")

class ProbabilityForm(forms.Form):
    a = forms.IntegerField(label="a")
    b = forms.IntegerField(label="b")
    c = forms.IntegerField(label="c")