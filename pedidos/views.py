from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def saludo(request):
    return HttpResponse("Hola a todos!")

def saludo_html(request):
    documento="""<html><body><h1>Hola a todos! - Tomado del archivo views.py de aplicación</h1></body></html>"""
    return HttpResponse(documento)

from django.template import Template,Context
import os
def saludo_plantilla(request):
    # arch=open("C:/Users/usuario/Desktop/Proyecto/Proyecto/templates/plantilla.html")
    # plt=Template(arch.read())
    # arch.close()
    # ctx=Context()
    # documento=plt.render(ctx)
    # return HttpResponse(documento)
    text="texto de prueba"
    name=os.getenv('USERNAME','a todos')
    return render(request,"plantilla.html",{"var1":name,"var2":text})

import datetime
def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(documento)

def sumar(request,n1,n2):
    suma=n1+n2
    documento="<html><body><h2>La suma de %s y %s es %s"%(n1,n2,suma)
    return HttpResponse(documento)

def curso(request):
    fecha = datetime.datetime.now()
    return render(request,"curso.html",{"now":fecha})