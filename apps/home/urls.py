from django.urls import path, include

from apps.home.views import home, inicio, nosotros

urlpatterns = [
    path('', home),
    path('inicio/', inicio),
    path('nosotros/', nosotros),
]