from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API.serializers.PreguntaSerializer import PreguntaInfo
from API.models import Pregunta
import json

@api_view(['GET','POST'])
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