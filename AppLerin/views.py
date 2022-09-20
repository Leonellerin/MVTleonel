from pydoc import doc
from django.http import HttpResponse
from django.shortcuts import render
from AppLerin.models import Padre, Madre, Hermano
from django.template import loader


def papa(self):
    papa1 = Padre(nombre='Cacho', edad='37', profesion='Panadero')
    papa1.save()
    resultado = f"Mi padre se llama {papa1.nombre},su edad es {papa1.edad}, y su trabajo es {papa1.profesion}"
    return HttpResponse(resultado)


def mama(self):
    mama1 = Madre(nombre='Patri', edad=24, profesion='Marinera')
    mama1.save()
    resultado = f"Mi madre se llama {mama1.nombre},su edad es {mama1.edad}, y su trabajo es {mama1.profesion}"
    return HttpResponse(resultado)


def hermano(self):
    bro1 = Hermano(nombre='Julian', edad=78, profesion='pebetero')
    bro1.save()
    resultado = f"Mi hermano se llama {bro1.nombre},su edad es {bro1.edad}, y su trabajo es {bro1.profesion}"
    return HttpResponse(resultado)
