from django.shortcuts import render
from .forms import NumbersForm

# Create your views here.


def index(request):

    if request.method == "POST":
        form = NumbersForm(request.POST)
        if form.is_valid():
            context = {'sum': form.cleaned_data['a'] + form.cleaned_data['b'] + form.cleaned_data['c']}
            context.update(form.cleaned_data)
            print("jzz context", context)
            return render(request, 'hello/index.html', context)

    context = {"name": 'unknown guest', 'form': NumbersForm()}
    return render(request, 'hello/index.html', context)
