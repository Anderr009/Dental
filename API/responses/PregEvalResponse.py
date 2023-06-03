from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from API.serializers.PreguntaEvSerializer import PregEvSerializer
from API.models import Pregunta_Evaluacion, Pregunta,Evaluacion
from json import loads

@api_view(['GET','POST'])
def PregEvResponse(request):
    if request.method == 'GET':
        pregEv = Pregunta_Evaluacion.objects.all()
        serializer_context ={
            'request':request
        }
        serializer = PregEvSerializer(pregEv,many=True,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #En caso de ser POST va  a recibir 
    # dos parametros y seran los ID de la 
    # pregunta y evaluacion correspondiente 
    if request.method == 'POST':
        data = loads(request.body)
        fk_preg = Pregunta.objects.get(cod=data['cod_preg']) #cod_preg es el primer parametro
        fk_ev = Evaluacion.objects.get(cod_ev=data['cod_ev']) #ese es el segundo parametro 
        objPregEv = {
            'fk_ev':fk_ev,
            'fk_pregunta':fk_preg
        }
        pregEv = Pregunta_Evaluacion(**objPregEv)
        pregEv.save()
        return Response({'mensaje':'creado'},status=status.HTTP_201_CREATED)