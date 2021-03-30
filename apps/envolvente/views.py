from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'envolvente/envolvente.html')

def normas(request):
    return render(request, 'envolvente/envolvente_nor.html')

def calculos(request):
    return render(request, 'envolvente/envolvente_calc.html')