# admin_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CursoViewSet, InscripcionViewSet, ProgresoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'progreso', ProgresoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
