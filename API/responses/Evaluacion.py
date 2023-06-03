from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from API.serializers.EvaluacionSerializer import EvaluacionSerializer
from API.models import Evaluacion
import json



@api_view(['GET','POST'])
def EvaluacionResponse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ev = Evaluacion(**data)
        ev.save()
        return Response({'mensaje':'creado'},status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        #se le debe pasar un json con el parametro cod_ev
        data = json.loads(request.body)
        id = data['cod_env']
        try:
            ev = Evaluacion.objects.get(cod_ev=id)
            serializer = EvaluacionSerializer(ev)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except (ObjectDoesNotExist):
            return Response({'mensaje':'No se encuentra la evaluacion solicitada'})