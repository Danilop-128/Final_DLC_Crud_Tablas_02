from django.urls import path 
from contacto_app import views 

urlpatterns = [
    path("contacto", views.inicio_vistaContacto,name="contacto"),
    path("registrarContacto/",views.registrarContacto,name="registrarContacto"),
    path("seleccionarContacto/<id>",views.seleccionarContacto,name="seleccionarContacto"),
    path("editarContacto/",views.editarContacto,name="editarContacto"),
    path("borrarContacto/<id>",views.borrarContacto,name="borrarContacto")
    
]