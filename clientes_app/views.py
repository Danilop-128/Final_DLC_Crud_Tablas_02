from django.shortcuts import render,redirect
from .models import Cliente

# Create your views here.

def inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarClientes.html",{"misclientes":losclientes})

def registrarCliente(request):
    id=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    celular=request.POST["numcelular"]
    direccion=request.POST["txtdireccion"]
    pedidos=request.POST["numpedidos"]
    fecha_inicio=request.POST["txtfecha_inicio"]

    guardarCliente=Cliente.objects.create(
        id=id,nombre=nombre,email=email,celular=celular,direccion=direccion,
        pedidos=pedidos,fecha_inicio=fecha_inicio
    )#GUARDA EL REGISTRO
    return redirect("clientes")

def seleccionarCliente(request,id):
    cliente=Cliente.objects.get(id=id)
    return render(request,"editarcliente.html",{"misclientes":cliente})

def editarCliente(request):
    id=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    celular=request.POST["numcelular"]
    direccion=request.POST["txtdireccion"]
    pedidos=request.POST["numpedidos"]
    fecha_inicio=request.POST["txtfecha_inicio"]
    cliente=Cliente.objects.get(id=id)
    cliente.nombre=nombre
    cliente.email=email
    cliente.celular=celular
    cliente.direccion=direccion
    cliente.pedidos=pedidos
    cliente.fecha_inicio=fecha_inicio

    cliente.save() # guarda registro actualizado
    return redirect("clientes")

def borrarCliente(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete() # borra el registro
    return redirect("clientes")
