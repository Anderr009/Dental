from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API.models import Procedimiento
from API.serializers.ProcedimientoSerializer import ProcedSerializer
import json
@api_view(['GET','POST','DELETE','PUT'])
def procedResponse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        proced = Procedimiento(**data)
        proced.save()
        return Response({'mensaje':'creado'},status=status.HTTP_200_OK)
    
    if request.method == 'GET':
        proceds = Procedimiento.objects.all()
        serializer = ProcedSerializer(proceds,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #En caso de que la peticion sea DELETE
    if request.method == 'DELETE':
        data = json.loads(request.body)
        proced = Procedimiento(**data)
        #--
        procedDel = Procedimiento.objets.get(cod_proced = proced.cod_proced)
        procedDel.delete()
        return Response({'msj':f'Eliminado satisfactoriamente Id: {proced.cod_proced}'},status= status.HTTP_200_OK)
    
    #En caso de que la peticion sea PUT
    if request.method == 'PUT':
        data = json.loads(request.body)
        proced = Procedimiento(**data)
        #--
        procedUpd = Procedimiento.objets.get(cod_proced = proced.cod_proced)
        procedUpd = proced
        procedUpd.save()
        return Response({'msj':'Actualizado correctamente'}, status = status.HTTP_201_CREATED)
