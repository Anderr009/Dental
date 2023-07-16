from django.urls import path
#responses de Cliente
from .responses.Client import BasicInfoClient,ClientComplete,EvaluacionesCliente
#resposnes de Preguntas de la evaluacion
from .responses.Pregunta import PreguntaResponse
#response de Evaluacion 
from .responses.Evaluacion import EvaluacionResponse
#response de procedimiento
from .responses.Procedimiento import procedResponse
#response de Pregunta/Evaluacion
from .responses.PregEvalResponse import PregEvResponse
#Proced_ev
from .responses.ProcedEval import procedEval
urlpatterns = [
    path('SearchClient/<str:ced>/',BasicInfoClient), #informacion para busqueda
    path('ClientComplete/', ClientComplete),#Cliente completo,
    path('Pregunta/',PreguntaResponse), #Introduce un json con los campos completos
    path('Evaluacion/',EvaluacionResponse), #Recibe un json con el campo cod_ev http://127.0.0.1:8000/API/Evaluacion/
    path('procedimiento/', procedResponse), #Procedimiento
    path('PregEvaluacion/', PregEvResponse), #Las preguntas que contienen una evaluacion
    path('ProcedEvaluacion/',procedEval),
    path('evaluacionCliente/<str:ced>',EvaluacionesCliente),
]
