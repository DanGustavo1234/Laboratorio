from django.contrib import admin
from .models import Estudiante, Docente,Carrera,Horario,Laboratorio, Materia, Biblioteca, Salasdelectura, Reserva_laboratorio, Reserva_biblioteca, Reserva_salasdelectura




admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Horario)
admin.site.register(Laboratorio)
admin.site.register(Carrera)
admin.site.register(Biblioteca)
admin.site.register(Reserva_laboratorio)
admin.site.register(Reserva_biblioteca)
admin.site.register(Reserva_salasdelectura)
admin.site.register(Materia)
admin.site.register(Salasdelectura)




