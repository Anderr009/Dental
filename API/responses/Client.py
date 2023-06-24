from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import json
from API.serializers.ClientSerializer import BasicClient,ListClient
from API.models import Cliente
#Vista para insertar un cliente o pedir su informacion completa
@api_view(['GET','POST','PUT','DELETE'])
def ClientComplete(request):
    if request.method == 'POST':
        #Obteniendo los datos del body
        data = request.body.decode('utf-8')
        #cargando el json
        dataDict = json.loads(data)
        #creando el obj cliente con el json obtenido
        cl = Cliente(**dataDict)
        cl.save()
        return Response({"mensaje":"Creado"},status=status.HTTP_201_CREATED)
    #--Si el request es DELETE
    if request.method == 'DELETE':
        data = request.body.decode('utf-8')
        #cargando json
        dataDict = json.loads(data)
        #buscando el obj
        clDel = Cliente.objects.get(id = dataDict['id'])
        #eliminando el obj
        clDel.delete();
        return  Response({"msj":f"Eliminado correctamente ID: {clDel.id} "},status= status.HTTP_200_OK)
    
    #-- Si el request es UPDATE
    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        dataDict = json.loads(data)
        #actualizando
        clNew = Cliente(**dataDict)
        #obteniendo cliente
        clUpdate = Cliente.objects.get(id=clNew.id)
        clUpdate = clNew
        clUpdate.save()
        return Response({"msj":"Actualizado correctamente"},status = status.HTTP_201_CREATED)
    #---Si el request es GET
    if request.method == 'GET':
        clients = Cliente.objects.all()
        serializer = ListClient(clients,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

#Vista basica del cliente para terminos de busqueda
@api_view(['GET'])
def BasicInfoClient(request,ced):
    if request.method == 'GET':
        try:
            #obteniendo el cliente 
            cl = Cliente.objects.get(cedula=ced)
        except ObjectDoesNotExist:
            return Response({'error':'Cliente no encontrado'},status=status.HTTP_404_NOT_FOUND)
        serializer= BasicClient(cl)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #-----------------------------------