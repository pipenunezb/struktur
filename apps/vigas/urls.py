from django.urls import path, include

from apps.vigas.views import index, normas, calculos

urlpatterns = [
    path('vigas/', index),
    path('vigas_normas/', normas),
    path('vigas_calculos/', calculos),
]