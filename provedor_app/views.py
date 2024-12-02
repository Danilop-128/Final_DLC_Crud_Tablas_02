from django.shortcuts import render,redirect
from .models import Proveedor

# Create your views here.

def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()
    return render(request,"gestionarProveedor.html",{"misproveedores":losproveedores})

def registrarProveedor(request):
    id=request.POST["numid"]
    celular=request.POST["numcelular"]
    direccion=request.POST["txtdireccion"]
    email=request.POST["txtemail"]
    tipo=request.POST["txttipo"]
    provincia=request.POST["txtprovincia"]
    nombre=request.POST["txtnombre"]

    guardarProveedor=Proveedor.objects.create(
        id=id,celular=celular,direccion=direccion,email=email,
        tipo=tipo,provincia=provincia,nombre=nombre,
    )#GUARDA EL REGISTRO

    return redirect("proveedor")

def seleccionarProveedor(request,id):
    proveedor=Proveedor.objects.get(id=id)
    return render(request,"editarproveedor.html",{"misproveedores":proveedor})

def editarProveedor(request):
    id=request.POST["numid"]
    celular=request.POST["numcelular"]
    direccion=request.POST["txtdireccion"]
    email=request.POST["txtemail"]
    tipo=request.POST["txttipo"]
    provincia=request.POST["txtprovincia"]
    nombre=request.POST["txtnombre"]
    proveedor=Proveedor.objects.get(id=id)
    proveedor.celular=celular
    proveedor.direccion=direccion
    proveedor.email=email
    proveedor.tipo=tipo
    proveedor.provincia=provincia
    proveedor.nombre=nombre

    proveedor.save() # guarda registro actualizado
    return redirect("proveedor")

def borrarProveedor(request,id):
    proveedor=Proveedor.objects.get(id=id)
    proveedor.delete() # borra el registro
    return redirect("proveedor")
