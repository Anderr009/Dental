from rest_framework import serializers
from API.models import Cliente
from API.serializers.EvaluacionSerializer import EvaluacionSerializer
#from rest_framework.decorators import api_view
#Serializador basico para buscar al cliente
class evaluacionCliente(serializers.ModelSerializer):
    evaluacion = EvaluacionSerializer(many=True, read_only=True, source='id')
    class Meta:
        model = Cliente
        fields = ['id','cedula','nombres','direccion','sexo','edad','apellido','evaluacion']