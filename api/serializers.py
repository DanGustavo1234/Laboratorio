from rest_framework import serializers
from .models import Estudiante, Docente,Carrera,Horario,Laboratorio, Materia, Biblioteca, Salasdelectura, Reserva_laboratorio, Reserva_biblioteca, Reserva_salasdelectura


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
        read_only_fields = ('id',)

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'
        read_only_fields = ('id',)

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'
        read_only_fields = ('id',)

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'
        read_only_fields = ('id',)

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'
        read_only_fields = ('id',)

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
        read_only_fields = ('id',)

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '__all__'
        read_only_fields = ('id',)

class SalasdelecturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salasdelectura
        fields = '__all__'
        read_only_fields = ('id',)

class Reserva_laboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva_laboratorio
        fields = '__all__'
        read_only_fields = ('id',)

class Reserva_bibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva_biblioteca
        fields = '__all__'
        read_only_fields = ('id',)

class Reserva_salasdelecturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva_salasdelectura
        fields = '__all__'
        read_only_fields = ('id',)
# Path: ControlLaboratorios\api\urls.py