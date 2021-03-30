from django.urls import path, include

from apps.diagramas.views import index, normas, calculos
urlpatterns = [
    path('diagramas/', index),
    path('diagramas_normas/', normas),
    path('diagramas_calculos/', calculos),
]