from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API.models import Eval_Proced,Evaluacion,Procedimiento
from API.serializers.EvalProcedSerializer import EvalProcedSerializer
import json
@api_view(['GET','POST','DELETE','PUT'])
def procedEval(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ev = Evaluacion.objects.get(cod_ev=data['cod_eval']['mensaje'])
        proc = Procedimiento.objects.get(cod_proced= data['cod_proc'])
        proced = Eval_Proced(cod_proc= proc,cod_eval = ev,pago_total = data['pago_total'],abono=data['abono'])
        proced.save()
        return Response({'mensaje':'creado'},status=status.HTTP_200_OK)
    
    if request.method == 'GET':
        proceds = Eval_Proced.objects.all()
        serializer = EvalProcedSerializer(proceds,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #En caso de que la peticion sea DELETE
    if request.method == 'DELETE':
        data = json.loads(request.body)
        proced = Eval_Proced(**data)
        #--
        procedDel = Eval_Proced.objects.get(cod_proced = proced.cod_proced)
        procedDel.delete()
        return Response({'msj':f'Eliminado satisfactoriamente Id: {proced.cod_proced}'},status= status.HTTP_200_OK)
    
    #En caso de que la peticion sea PUT
    if request.method == 'PUT':
        data = json.loads(request.body)
        proced = Eval_Proced(**data)
        #--
        procedUpd = Eval_Proced.objects.get(cod_proced = proced.cod_proced)
        procedUpd = proced
        procedUpd.save()
        return Response({'msj':'Actualizado correctamente'}, status = status.HTTP_201_CREATED)
