from django.urls import path 
from provedor_app import views 

urlpatterns = [
    path("proveedor", views.inicio_vistaProveedor,name="proveedor"),
    path("registrarProveedor/",views.registrarProveedor,name="registrarProveedor"),
    path("seleccionarProveedor/<id>",views.seleccionarProveedor,name="seleccionarProveedor"),
    path("editarProveedor/",views.editarProveedor,name="editarProveedor"),
    path("borrarProveedor/<id>",views.borrarProveedor,name="borrarProveedor")
    
]