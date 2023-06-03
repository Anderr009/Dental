from rest_framework.serializers import HyperlinkedModelSerializer
from .ProcedimientoSerializer import ProcedSerializer
from .EvaluacionSerializer import EvaluacionSerializer
from API.models import Eval_Proced

class EvalProcedSerializer(HyperlinkedModelSerializer):
    fk_proc = ProcedSerializer()
    fk_ev = EvaluacionSerializer()
    class Meta:
        model = Eval_Proced
        fields= '__all__'
