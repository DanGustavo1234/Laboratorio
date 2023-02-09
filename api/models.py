from django.db import models

# Create your models here.

class Persona(models.Model):

    TIPO=[
        ('CEDULA','Cedula'),
        ('PASAPORTE','Pasaporte'),
    ]

    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    documento_identidad = models.CharField(max_length=50,choices=TIPO ,blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50,  blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField( blank=True, null=True)
    pais_origen = models.CharField(max_length=50, blank=True, null=True)
    
    


class Carrera(models.Model):
    CARRERA=[
        ('AGRONEGOCIOS','Agronegocios'),
        ('ADMINISTRACION DE EMPRESAS','Administracion de Empresas'),
        ('NEGOCIOS INTERNACIONALES','Negocios Internacionales'),
        ('MARKETING','Marketing'),
        ('ARQUITECTURA','Arquitectura'),
        ('DERECHO','Derecho'),
        ('TECNOLOGIAS DE LA INFORMACION Y COMUNICACION','Tecnologias de la Informacion y Comunicacion'),
        ('TURISMO', 'Turismo'),
        ('PSICOLOGIA','Psicologia'), 
    ]
    nombre_carrera = models.CharField(max_length=50,choices=CARRERA,blank=True, null=True)
    duracion=models.PositiveSmallIntegerField( default=5,blank=True, null=True)

    def __str__(self):
        return self.nombre_carrera

class Laboratorio(models.Model):

    ESTADO=[
        ('DIPONIBLE','Disponible'),
        ('OCUPADO','Ocupado'),
    ]

    nombre = models.CharField(max_length=50, blank=True, null=True)
    numero_de_maquinas=models.PositiveSmallIntegerField( default=5,blank=True, null=True)
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50,choices=ESTADO,blank=True, null=True)

    def __str__(self):
        return self.nombre

class Biblioteca(models.Model):

    ESTADO=[
         ('DIPONIBLE','Disponible'),
        ('OCUPADO','Ocupado'),
    ]

    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50)
    numero_de_maquinas=models.PositiveSmallIntegerField( default=5,blank=True, null=True)
    estado = models.CharField(max_length=50,choices=ESTADO,blank=True, null=True)

    def __str__(self):
        return self.nombre

class Salasdelectura(models.Model):

    ESTADO=[
         ('DIPONIBLE','Disponible'),
        ('OCUPADO','Ocupado'),
    ]

    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion= models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

     

class Estudiante(Persona):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    foto_estudiante = models.ImageField(upload_to='static/fotos_estudiante', blank=True, null=True)

    def __str__(self):
           return  self.nombre +' '+ self.apellido

class Docente(Persona):
    carrera = models.ManyToManyField(Carrera, blank=True)
    foto_docente = models.ImageField(upload_to='static/fotos_docente', blank=True, null=True)

    def __str__(self):
        return  self.nombre +' '+ self.apellido


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    docente=models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, null=True)
    carrera=models.ForeignKey( Carrera, on_delete=models.CASCADE, blank=True, null=True)
    estudiante=models.ManyToManyField(Estudiante, blank=True)

    def __str__(self):
        return self.nombre

class Reserva_laboratorio(models.Model):
    estudiante=models.ManyToManyField(Estudiante, blank=True, null=True)
    docente=models.ManyToManyField(Docente, blank=True, null=True)
    laboratorio=models.ForeignKey(Laboratorio, on_delete=models.CASCADE, blank=True, null=True)
    carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField( blank=True, null=True)
    hora_fin = models.DateTimeField( blank=True, null=True)
    
    def __str__(self):
        return self.laboratorio.nombre +' '+ self.materia.nombre + ' '+self.carrera.nombre_carrera +' '+ self.materia.carrera.nombre + ' ' + self.dia +' ' + self.hora_inicio + ' ' + self.hora_fin

class Reserva_biblioteca(models.Model):

    NUMERO_MAQUINAS=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7')
    ]

    biblioteca=models.ForeignKey(Biblioteca, on_delete=models.CASCADE, blank=True, null=True)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE, blank=True, null=True)
    docente=models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, null=True)
    carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE)
    numero_maquina=models.CharField(max_length=50,choices=NUMERO_MAQUINAS,blank=True, null=True)
    hora_inicio = models.DateTimeField( blank=True, null=True)
    hora_fin = models.DateTimeField( blank=True, null=True)
    
    def __str__(self):
        return self.laboratorio.nombre +' '+ self.materia.nombre + ' '+self.carrera.nombre_carrera +' '+ self.materia.carrera.nombre + ' ' + self.dia +' ' + self.hora_inicio + ' ' + self.hora_fin

class Reserva_salasdelectura(models.Model):
    salasdelectura=models.ForeignKey(Salasdelectura, on_delete=models.CASCADE, blank=True, null=True)
    estudiante=models.ManyToManyField(Estudiante, blank=True, null=True)
    docente=models.ManyToManyField(Docente, blank=True, null=True)
    carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField( blank=True, null=True)
    hora_fin = models.DateTimeField( blank=True, null=True)
    
    def __str__(self):
        return self.laboratorio.nombre +' '+ self.materia.nombre + ' '+self.carrera.nombre_carrera +' '+ self.materia.carrera.nombre + ' ' + self.dia +' ' + self.hora_inicio + ' ' + self.hora_fin



class Horario(models.Model):
    laboratorio=models.ForeignKey(Laboratorio, on_delete=models.CASCADE, blank=True, null=True)
    biblioteca=models.ForeignKey(Biblioteca, on_delete=models.CASCADE, blank=True, null=True)
    salasdelectura=models.ForeignKey(Salasdelectura, on_delete=models.CASCADE, blank=True, null=True)
    fecha=models.DateField( blank=True, null=True)
    hora_inicio = models.DateTimeField( blank=True, null=True)
    hora_fin = models.DateTimeField( blank=True, null=True)
    

    def __str__(self):
        return self.laboratorio.nombre +' '+ self.fecha +' '+ self.hora_inicio + ' ' + self.hora_fin








