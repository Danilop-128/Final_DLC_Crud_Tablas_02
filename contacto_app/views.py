from django.shortcuts import render,redirect
from .models import Contacto

# Create your views here.

def inicio_vistaContacto(request):
    loscontactos=Contacto.objects.all()
    return render(request,"gestionarContacto.html",{"miscontactos":loscontactos})

def registrarContacto(request):
    id=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    email=request.POST["txtemail"]
    celular=request.POST["numcelular"]
    direccion=request.POST["txtdireccion"]
    url_web=request.POST["txturl_web"]

    guardarContacto=Contacto.objects.create(
    id=id,nombre=nombre,apellidos=apellidos,email=email,celular=celular,direccion=direccion,
    url_web=url_web
    )#GUARDA EL REGISTRO

    return redirect("contacto")

def seleccionarContacto(request,id):
    contacto=Contacto.objects.get(id=id)
    return render(request,"editarcontacto.html",{"miscontactos":contacto})

def editarContacto(request):
    id=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    email=request.POST["txtemail"]
    celular=request.POST["numcelular"]
    direccion=request.POST["txtdireccion"]
    url_web=request.POST["txturl_web"]
    contacto=Contacto.objects.get(id=id)
    contacto.nombre=nombre
    contacto.apellidos=apellidos
    contacto.email=email
    contacto.celular=celular
    contacto.direccion=direccion
    contacto.url_web=url_web
    contacto.save() # guarda registro actualizado
    return redirect("contacto")

def borrarContacto(request,id):
    contacto=Contacto.objects.get(id=id)
    contacto.delete() # borra el registro
    return redirect("contacto")
