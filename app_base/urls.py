from django.urls import path
from app_base import views

urlpatterns=[
    #inicio tienda
    path('',views.inicio),
]