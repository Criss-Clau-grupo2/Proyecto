from django.urls import path
from . import views

urlpatterns = [
    path('',views.cuenta,name='cuenta'),
    path('registro',views.registro,name='registro'),
]