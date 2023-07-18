from rest_framework import serializers
from API.models import Cliente, Procedimiento, Pregunta, Evaluacion, Pregunta_Evaluacion, Eval_Proced
from API.serializers.EvaluacionSerializer import EvaluacionSerializer
from API.serializers.ProcedimientoSerializer import ProcedSerializer
from API.serializers.PreguntaEvSerializer import PregEvSerializer
from API.serializers.EvalProcedSerializer import EvalProcedSerializer

class evaluacionCliente(serializers.ModelSerializer):
    evaluacion_set = serializers.SerializerMethodField()

    def get_evaluacion_set(self, cliente):
        evaluaciones = cliente.evaluacion_set.all()
        evaluaciones_data = EvaluacionSerializer(evaluaciones, many=True).data
        for evaluacion_data in evaluaciones_data:
            cod_eval = evaluacion_data['cod_ev']
            procedimientos = Procedimiento.objects.filter(eval_proced__cod_eval_id=cod_eval)
            procedimientos_data = ProcedSerializer(procedimientos, many=True).data
            for procedimiento_data in procedimientos_data:
                if eval_proced:
                    procedimiento_data['pago_total'] = eval_proced.pago_total
                    procedimiento_data['abono'] = eval_proced.abono
            evaluacion_data['procedimientos'] = procedimientos_data
            preguntas_evaluacion = Pregunta_Evaluacion.objects.filter(fk_ev_id=cod_eval)
            preguntas_data = PregEvSerializer(preguntas_evaluacion, many=True).data
            eval_proced = Eval_Proced.objects.filter(cod_eval_id=cod_eval).first()
            evaluacion_data['preguntas_evaluacion'] = preguntas_data
        return evaluaciones_data

    class Meta:
        model = Cliente
        fields = ['id', 'cedula', 'nombres', 'direccion', 'sexo', 'edad', 'apellido', 'evaluacion_set']
    