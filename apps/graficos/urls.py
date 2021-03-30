from django.urls import path, include

from apps.graficos.views import index, normas, calculos

urlpatterns = [
    path('graficos/', index),
    path('graficos_normas/', normas),
    path('graficos_calculos/', calculos),
]