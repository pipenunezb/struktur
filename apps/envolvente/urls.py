from django.urls import path, include

from apps.envolvente.views import index, normas, calculos

urlpatterns = [
    path('envolvente/', index),
    path('envolvente_normas/', normas),
    path('envolvente_calculos/', calculos),
]