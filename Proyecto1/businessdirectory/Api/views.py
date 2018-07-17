from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from RuteandoApi.models import Cities, Business
from RuteandoApi.serializers import CitiesSerializer, BusinessSerializer

# Create your views here.

# class BusinessList(generics.ListCreateAPIView):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer

# class CitiesList(generics.ListCreateAPIView):
#     queryset = Cities.objects.all()
#     serializer_class = CitiesSerializer


#serializers

# from rest_framework import serializers
# from RuteandoApi.models import Cities, Business

# class CitiesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cities
#         fields = ('nombre','departamento','pais')

# class BusinessSerializer(serializers.ModelSerializer):
#     # ciudadid = serializers.PrimaryKeyRelatedField(many=True,read_only=True,allow_null=True)    
#     class Meta:
#         model = Business
#         fields = ('nombre','direccion','ciudadid','telefono','descripcion')