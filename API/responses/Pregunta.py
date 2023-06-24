from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API.serializers.PreguntaSerializer import PreguntaInfo
from API.models import Pregunta
import json

@api_view(['GET','POST','PUT','DELETE'])
def PreguntaResponse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pr = Pregunta(**data)
        pr.save()
        return Response({'mensaje':'creado'},status = status.HTTP_201_CREATED)
    if request.method == 'GET':
        pr = Pregunta.objects.all()
        serializer = PreguntaInfo(pr, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #En caso de ser DELETE
    if request.method == 'DELETE':
        data = request.body.decode('utf-8')
        dataDict = json.loads(data)
        preguntaObj = Pregunta(**dataDict)
        #obteniendo la pregunta de la BD
        preguntaDel = Pregunta.objects.get(cod = preguntaObj.cod)
        #eliminando la pregunta de la BD
        preguntaDel.delete()
        return Response({"msj":f"Eliminado satisfactoriamente Id: {preguntaObj.cod}"}, status = status.HTTP_200_OK)
    #En caso de ser PUT
    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        dataDict = json.loads(data)
        preguntaObj = Pregunta(**dataDict)
        #Obteniendo la pregunta a actualizar de la BD
        preguntaUpd = Pregunta.objects.get(cod=preguntaObj.cod)
        preguntaUpd = preguntaObj
        preguntaUpd.save()
        return Response({"msj":"Actualizado correctamente"}, status = status.HTTP_201_OK)
    