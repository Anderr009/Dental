from rest_framework.serializers import ModelSerializer
from API.models import Evaluacion 

class EvaluacionSerializer(ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'
