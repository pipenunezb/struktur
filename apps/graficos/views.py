from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'graficos/graficos.html')

def normas(request):
    return render(request, 'graficos/graficos_nor.html')

def calculos(request):
    return render(request, 'graficos/graficos_calc.html')