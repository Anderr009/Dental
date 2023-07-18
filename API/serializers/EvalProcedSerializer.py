from rest_framework.serializers import ModelSerializer
from API.models import Eval_Proced

class EvalProcedSerializer(ModelSerializer):
    class Meta:
        model = Eval_Proced
        fields = '__all__'