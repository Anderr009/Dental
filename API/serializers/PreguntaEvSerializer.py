from rest_framework import serializers
from API.models import Pregunta_Evaluacion
#serializer de evaluacion
from .EvaluacionSerializer import EvaluacionSerializer
#serializer de Pregunta
from .PreguntaSerializer import PreguntaInfo

class PregEvSerializer(serializers.ModelSerializer):
    fk_ev = EvaluacionSerializer()
    fk_pregunta = PreguntaInfo()
    class Meta:
        model = Pregunta_Evaluacion
        fields = ['cod','fk_ev','fk_pregunta','respuesta']