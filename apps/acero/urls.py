from django.urls import path, include

from apps.acero.views import index, normas, calculos

urlpatterns = [
    path('acero/', index),
    path('acero_normas/', normas),
    path('acero_calculos/', calculos),
]