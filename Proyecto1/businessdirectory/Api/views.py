# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from rest_framework import generics
from django.views import generic
from django.views.generic import TemplateView, ListView
from Api.models import *
from Api.serializers import *

# Create your views here.
def index(request):
    posts = Ciudad.objects.all()
    return render(request, 'api/index.html')

class aa(ListView):
    model = Ciudad
    template_name = 'api/index.html'

#def registration(request):
#    return render(request, 'registration/registration_form.html')
   
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