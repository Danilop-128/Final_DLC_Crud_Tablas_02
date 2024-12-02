from django.shortcuts import render,redirect
from .models import Empleado

# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleados(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    direccion=request.POST["txtdireccion"]
    celular=request.POST["numcelular"]
    sueldo=request.POST["numsueldo"]
    horario=request.POST["txthorario"]

    guardarEmpleados=Empleado.objects.create(
        id=id,nombre=nombre,apellidos=apellidos,direccion=direccion,celular=celular,sueldo=sueldo,horario=horario
    )#GUARDA EL REGISTRO

    return redirect("empleado")

def seleccionarEmpleados(request,id):
    empleado=Empleado.objects.get(id=id)
    return render(request,"editarempleados.html",{"misempleados":empleado})




def editarEmpleados(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    direccion=request.POST["txtdireccion"]
    celular=request.POST["numcelular"]
    sueldo=request.POST["numsueldo"]
    horario=request.POST["numhorario"]
    empleado=Empleado.objects.get(id=id)
    empleado.nombre=nombre
    empleado.apellidos=apellidos
    empleado.direccion=direccion
    empleado.celular=celular
    empleado.sueldo=sueldo
    empleado.horario=horario
    empleado.save() # guarda registro actualizado
    return redirect("empleado")



def borrarEmpleados(request,id):
    empleado=Empleado.objects.get(id=id)
    empleado.delete() # borra el registro
    return redirect("empleado")
