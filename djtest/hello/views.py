from django.shortcuts import render
from .forms import NumbersForm
from math import *
# Create your views here.


def index(request):

    if request.method == "POST":
        form = NumbersForm(request.POST)
        if form.is_valid():
            context = {"d": form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c']}
            render(request, 'hello/index.html', context)
            if context['d']>=0:
                context = {"d": form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c'],'x1': (sqrt(form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c'])-form.cleaned_data['b'])/(2*form.cleaned_data['a']), 'x2': (-sqrt(form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c'])-form.cleaned_data['b'])/(2*form.cleaned_data['a'])}
                context.update(form.cleaned_data)
                print("jzz context", context)
                return render(request, 'hello/index.html', context)

    context = {"name": 'unknown guest', 'form': NumbersForm()}
    return render(request, 'hello/index.html', context)
