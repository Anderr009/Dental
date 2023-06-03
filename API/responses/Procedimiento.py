from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API.models import Procedimiento
from API.serializers.ProcedimientoSerializer import ProcedSerializer
import json
@api_view(['GET','POST'])
def procedResponse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        proced = Procedimiento(**data)
        proced.save()
        return Response({'mensaje':'creado'},status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        proceds = Procedimiento.objects.all()
        serializer = ProcedSerializer(proceds,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    