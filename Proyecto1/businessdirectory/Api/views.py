# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from django.views import generic
from django.views.generic import TemplateView
from Api.models import * #traer modelo
from Api.serializers import *#traer serializers

# Create your views here.

class CiudadList(generics.ListCreateAPIView):  #get post
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class CiudadDetail(generics.RetrieveDestroyAPIView):  #detele, put
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class TipoList(generics.ListCreateAPIView):  #get post
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class EmpresasList(generics.ListCreateAPIView):  #get post
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class ViewHome(generic.DetailView):
    # queryset = Ciudad
    template_name = 'consultas/home/'

class ViewPrueba(TemplateView):
    template_name = 'consultas/vista2/'