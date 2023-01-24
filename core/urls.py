from django.urls import path
from . import views
from .views import salvar

urlpatterns=[
    path('', views.index, name='index'),
    path('salvar/', salvar, name="salvar"),
]