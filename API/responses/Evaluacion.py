from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from API.serializers.EvaluacionSerializer import EvaluacionSerializer
from API.models import Evaluacion
import json



@api_view(['GET','POST','PUT','DELETE'])
def EvaluacionResponse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ev = Evaluacion(**data)
        ev.save()
        return Response({'mensaje':'creado'},status=status.HTTP_201_CREATED)
    #- En caso de que la peticion sea Delete
    if request.method == 'DELETE':
        data = request.body.decode('utf-8')
        dataDict = json.loads(data)
        evDel = Evaluacion.objects.get(cod_ev=dataDict.cod_ev)
        evDel.delete()
        return Response({"msj":f"Eliminado correctamente la evaluacion Id: {evDel.cod_ev}"})
    #- En caso de que el request sea un UPDATE
    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        dataDict = json.load(data)
        evUpd = Evaluacion(**dataDict)
        #obteniendo el obj de la base de datos para reemplazarlo
        ev = Evaluacion.objects.get(cod_ev= evUpd.cod_ev)
        ev = evUpd
        ev.save()
        return Response({"msj":"Actualizado correctamente"},status=status.HTTP_201_CREATED)
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