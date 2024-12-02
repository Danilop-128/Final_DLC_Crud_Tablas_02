from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.
def inicio_vistaProducto(request):
    losproductos=Producto.objects.all()
    return render(request,"gestionarProductos.html",{"misproductos":losproductos})

def registrarProducto(request):
    id=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["numprecio"]
    marca=request.POST["txtmarca"]
    stock=request.POST["numstock"]
    descripcion=request.POST["txtdescripcion"]

    guardarProducto=Producto.objects.create(
    id=id,nombre=nombre,precio=precio,marca=marca,stock=stock,descripcion=descripcion
    )#GUARDA EL REGISTRO

    return redirect("productos")

def seleccionarProducto(request,id):
    producto=Producto.objects.get(id=id)
    return render(request,"editarproducto.html",{"misproductos":producto})




def editarProducto(request):
    id=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["numprecio"]
    marca=request.POST["txtmarca"]
    stock=request.POST["numstock"]
    descripcion=request.POST["txtdescripcion"]
    producto=Producto.objects.get(id=id)
    producto.nombre=nombre
    producto.precio=precio
    producto.marca=marca
    producto.stock=stock
    producto.descripcion=descripcion
    producto.save() # guarda registro actualizado
    return redirect("productos")



def borrarProducto(request,id):
    producto=Producto.objects.get(id=id)
    producto.delete() # borra el registro
    return redirect("productos")


