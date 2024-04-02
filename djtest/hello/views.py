from django.shortcuts import render
from .forms import SquareForm, ProbabilityForm
from math import *
# Create your views here.


def square(request):

    if request.method == "POST":
        form = SquareForm(request.POST)
        if form.is_valid():
            context = {"d": form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c']}
            render(request, 'hello/square.html', context)
            if context['d']>=0:
                context = {"d": form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c'],'x1': (sqrt(form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c'])-form.cleaned_data['b'])/(2*form.cleaned_data['a']), 'x2': (-sqrt(form.cleaned_data['b']**2-4*form.cleaned_data['a']*form.cleaned_data['c'])-form.cleaned_data['b'])/(2*form.cleaned_data['a'])}
                context.update(form.cleaned_data)
                print("jzz context", context)
                return render(request, 'hello/square.html', context)
            else:

                return render(request, 'hello/square.html', context)

    context = {"name": 'unknown guest', 'form': SquareForm()}
    return render(request, 'hello/square.html', context)


def main_page(request):
    return render(request, "hello/main_page.html", {})


def probability(request):

    if request.method == "POST":
        form = ProbabilityForm(request.POST)
        if form.is_valid():
            c = {'c': factorial(form.cleaned_data['n']) / (factorial(form.cleaned_data['n'] - form.cleaned_data['k']) * factorial(form.cleaned_data['k']))}
            Q = {'q': 1-form.cleaned_data['p']}
            context = {'q': Q['q'], 'C': c['c'], 'P': c['c'] * form.cleaned_data['p'] ** form.cleaned_data['k'] * Q['q'] ** (form.cleaned_data['n'] - form.cleaned_data['k'])}
            context.update(form.cleaned_data)
            print("jzz context", context)
            return render(request, 'hello/probability.html', context,)

    context = {"name": 'unknown guest', 'form': ProbabilityForm()}
    return render(request, 'hello/probability.html', context,)