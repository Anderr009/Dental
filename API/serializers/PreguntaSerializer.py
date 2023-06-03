from rest_framework.serializers import ModelSerializer
from API.models import Pregunta

class PreguntaInfo(ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'