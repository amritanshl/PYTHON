from django.urls import path
from . import views

urlpatterns = [
    path('calculation', views.calculator, name='calculation')
]