from django.forms.forms import Form
from gestor.models import Items
from django.http import HttpResponse
import datetime
from django.template import loader
from django.shortcuts import render

from gestor.models import Items
from gestor.forms import Form1


class Persona(object):

    def __init__(self,nombre, apellido ):
        self.nombre = nombre
        self.apellido  = apellido
        self.lista = ['a','b','c','e']

def hija1 (request):
    p2 = Persona('Enrique','Gomez')
    data = {'user': p2, 'form' : Form1 }
    return render(request,'hija1.html',data)

def search(request):
    # r = request.POST['input']
    # data  = Items.objects.filter(id=r)
    # return HttpResponse(data)
    if request.method == 'POST':
        form = Form1(request.POST)

        if form.is_valid():
            dataForm = form.cleaned_data
            return HttpResponse('ok') 
    else:
        form = Form1()



    return render(request,'hija1.html',form)

    


def saludo(request): #una vista

    p1 = Persona('Juan','Perez')

    #nombre = 'Manuelsss'
    #apellido  = 'Barrios'

    
    #template = open('/code/composeexample/templates/mitemplate.html')
    #plt = Template(template.read())
    #template.close()

    #template = loader.get_template('mitemplate.html')

    data = {'persona' : p1 }

    #ctx = Context(data)
    #documento =  template.render(data)

    #return HttpResponse(documento)
    return render(request, 'mitemplate.html',data)

def chau(request, ano, actual):

    fecha = datetime.datetime.now()
    edadActual = actual
    periodo = ano-2021
    edadFutra = edadActual + periodo 

    return HttpResponse(edadFutra)