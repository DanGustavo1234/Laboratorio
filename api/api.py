from .models import Estudiante
from rest_framework import viewsets, permissions
from .models import Estudiante, Docente,Carrera,Horario,Laboratorio, Materia, Biblioteca, Salasdelectura, Reserva_laboratorio, Reserva_biblioteca, Reserva_salasdelectura
from .serializers import EstudianteSerializer, DocenteSerializer, CarreraSerializer, HorarioSerializer, LaboratorioSerializer, MateriaSerializer, BibliotecaSerializer, SalasdelecturaSerializer, Reserva_laboratorioSerializer, Reserva_bibliotecaSerializer, Reserva_salasdelecturaSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EstudianteSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DocenteSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarreraSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HorarioSerializer

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LaboratorioSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MateriaSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BibliotecaSerializer

class SalasdelecturaViewSet(viewsets.ModelViewSet):
    queryset = Salasdelectura.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SalasdelecturaSerializer

class Reserva_laboratorioViewSet(viewsets.ModelViewSet):
    queryset = Reserva_laboratorio.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Reserva_laboratorioSerializer

class Reserva_bibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Reserva_biblioteca.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Reserva_bibliotecaSerializer

class Reserva_salasdelecturaViewSet(viewsets.ModelViewSet):
    queryset = Reserva_salasdelectura.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Reserva_salasdelecturaSerializer

# Path: ControlLaboratorios\api\urls.py