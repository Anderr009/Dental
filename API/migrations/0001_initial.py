# Generated by Django 4.2.1 on 2023-05-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.TextField(max_length=12)),
                ('nombres', models.TextField(db_column='Nombre', max_length=100)),
                ('apellido', models.TextField(db_column='Apellido', max_length=100)),
                ('direccion', models.TextField(db_column='Direccion', max_length=300)),
                ('sexo', models.CharField(db_column='Sexo', max_length=1)),
                ('edad', models.IntegerField(db_column='Edad')),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('cod_ev', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(db_column='Fecha')),
                ('plan_tratamiento', models.TextField(db_column='Tratamiento')),
            ],
            options={
                'db_table': 'Evaluacion',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.TextField(db_column='Pregunta', max_length=200)),
            ],
            options={
                'db_table': 'Pregunta',
            },
        ),
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('cod_proced', models.AutoField(primary_key=True, serialize=False)),
                ('proced', models.TextField(db_column='Procedimiento', max_length=100)),
            ],
            options={
                'db_table': 'Procedmiento',
            },
        ),
    ]
