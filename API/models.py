from django.db import models
from django.utils.timezone import now
from datetime import date
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.TextField(max_length=12)
    nombres = models.TextField(max_length=100,db_column="Nombre")
    apellido = models.TextField(max_length=100,db_column="Apellido")
    direccion = models.TextField(max_length=300,db_column="Direccion")
    sexo = models.CharField(max_length=1,db_column="Sexo")
    edad = models.IntegerField(db_column="Edad")
    class Meta:
        db_table='Cliente'
    #---------------------------


class Evaluacion(models.Model):
    cod_ev = models.AutoField(primary_key=True)
    fecha = models.DateField(db_column="Fecha",default=now)
    plan_tratamiento = models.TextField(db_column="Tratamiento",null=False)
    class Meta:
        db_table='Evaluacion'
    #---------

class Procedimiento(models.Model):
    cod_proced = models.AutoField(primary_key=True)
    proced = models.TextField(max_length=100, db_column="Procedimiento")
    class Meta:
        db_table="Procedmiento"

class Pregunta(models.Model):
    cod = models.AutoField(primary_key=True)
    pregunta = models.TextField(max_length=200,db_column="Pregunta")
    class Meta:
        db_table='Pregunta'
# Tabla intermedia
class Pregunta_Evaluacion(models.Model):
    cod = models.AutoField(primary_key=True)
    fk_ev  = models.ForeignKey(Evaluacion,on_delete=models.CASCADE)
    fk_pregunta  = models.ForeignKey(Pregunta,on_delete=models.CASCADE)    
    #----Clase Meta
    class Meta:
        db_table='Pregunta_Evaluacion'
# Tabla intermedia
class Eval_Proced:
    cod = models.AutoField(primary_key=True)
    cod_proc = models.ForeignKey(Procedimiento,on_delete=models.CASCADE)
    cod_eval = models.ForeignKey(Evaluacion,on_delete=models.CASCADE)
    pago_total = models.FloatField()
    abono = models.FloatField()
    #---Clase Meta
    class Meta:
        db_table='Eval_Proced'