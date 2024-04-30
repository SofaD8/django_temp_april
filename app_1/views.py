from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>App 1</h1>')


def main(request):
    context = {
        'years': (2020, 2021, 2022, 2023, 2024),
    }

    return render(request, 'index.html', context=context)