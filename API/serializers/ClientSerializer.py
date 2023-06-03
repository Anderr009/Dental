from rest_framework import serializers
from API.models import Cliente
#from rest_framework.decorators import api_view
#Serializador para la lista de pacientes 
class ListClient(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
#Serializador basico para buscar al cliente
class BasicClient(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','cedula','nombres','apellido']