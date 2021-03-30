from django.urls import path, include

from apps.columnas.views import index, normas, calculos

urlpatterns = [
    path('columnas/', index),
    path('columnas_normas/', normas),
    path('columnas_calculos/', calculos),
]