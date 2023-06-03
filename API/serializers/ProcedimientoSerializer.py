from rest_framework import serializers
from API.models import Procedimiento

class ProcedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento
        fields = '__all__'