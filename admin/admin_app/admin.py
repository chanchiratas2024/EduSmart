# admin_app/admin.py
from django.contrib import admin
from .models import Usuario, Curso, Inscripcion, Progreso

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'apellido', 'correo', 'rol', 'fecha_registro')
    list_filter = ('rol',)
    search_fields = ('nombre', 'apellido', 'correo')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'nombre', 'categoria', 'fecha_inicio', 'fecha_fin', 'docente')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'usuario', 'curso', 'estado', 'fecha_inscripcion')
    list_filter = ('estado',)
    search_fields = ('usuario__nombre', 'curso__nombre')

@admin.register(Progreso)
class ProgresoAdmin(admin.ModelAdmin):
    list_display = ('id_progreso', 'usuario', 'curso', 'porcentaje_avance', 'ultima_actividad')
    list_filter = ('curso',)
    search_fields = ('usuario__nombre', 'curso__nombre')
