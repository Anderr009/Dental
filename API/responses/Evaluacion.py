from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from API.serializers.EvaluacionSerializer import EvaluacionSerializer
from API.models import Evaluacion,Cliente
import json



@api_view(['GET','POST','PUT','DELETE'])
def EvaluacionResponse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cl = Cliente.objects.get(id =data['cod_cl'])
        ev = Evaluacion(cod_cl= cl,plan_tratamiento =data['plan_tratamiento'])
        ev.save()
        cod = ev.cod_ev
        return Response({'mensaje':cod},status=status.HTTP_201_CREATED)
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
        try:
            ev = Evaluacion.objects.all()
            serializer = EvaluacionSerializer(ev,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except (ObjectDoesNotExist):
            return Response({'mensaje':'No se encuentra la evaluacion solicitada'})