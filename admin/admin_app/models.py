# admin_app/models.py
from django.db import models

class Usuario(models.Model):
    ROLES = [('admin','admin'),('alumno','alumno'),('docente','docente')]
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña_hash = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=ROLES)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'  # coincide con tu tabla en MySQL

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    docente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, db_column='docente_id', limit_choices_to={'rol':'docente'})

    class Meta:
        db_table = 'cursos'

class Inscripcion(models.Model):
    ESTADOS = [('activo','activo'),('completado','completado'),('abandonado','abandonado')]
    id_inscripcion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='id_curso')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')

    class Meta:
        db_table = 'inscripciones'

class Progreso(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='id_curso')
    porcentaje_avance = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ultima_actividad = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'progreso'
