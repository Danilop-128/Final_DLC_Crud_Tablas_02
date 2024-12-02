from django.shortcuts import render,redirect
from .models import Venta

# Create your views here.

def inicio_vistaVenta(request):
    lasventas=Venta.objects.all()
    return render(request,"gestionarVentas.html",{"misventas":lasventas})

def registrarVenta(request):
    id_venta=request.POST["numid_venta"]
    id_empleado=request.POST["txtid_empleado"]
    id_cliente=request.POST["numid_cliente"]
    id_producto=request.POST["numid_producto"]
    fecha_venta=request.POST["txtfecha_venta"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]

    guardarVenta=Venta.objects.create(
    id_venta=id_venta, id_empleado=id_empleado,id_cliente=id_cliente,id_producto=id_producto,fecha_venta=fecha_venta,cantidad=cantidad,total=total
    )#GUARDA EL REGISTRO

    return redirect("venta")

def seleccionarVenta(request,id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    return render(request,"editarventas.html",{"misventas":venta})

def editarVenta(request):
    id_venta=request.POST["numid_venta"]
    id_empleado=request.POST["txtid_empleado"]
    id_cliente=request.POST["numid_cliente"]
    id_producto=request.POST["numid_producto"]
    fecha_venta=request.POST["txtfecha_venta"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]
    venta=Venta.objects.get(id_venta=id_venta)
    venta.id_empleado=id_empleado
    venta.id_cliente=id_cliente
    venta.id_producto=id_producto
    venta.fecha_venta=fecha_venta
    venta.cantidad=cantidad
    venta.total=total
    venta.save() # guarda registro actualizado
    return redirect("/venta")

def borrarVenta(request,id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    venta.delete() # borra el registro
    return redirect("venta")


