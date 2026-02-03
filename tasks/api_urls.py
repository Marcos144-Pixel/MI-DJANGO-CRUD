from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    PerfilViewSet, ExperienciaViewSet, CursoViewSet,
    ReconocimientoViewSet, ProductoViewSet, ProductoLaboralViewSet,
    ProductoAcademicoViewSet, TaskViewSet, VentaGarajeViewSet, cv_completo
)

# Crear el router y registrar los viewsets
router = DefaultRouter()
router.register(r'perfiles', PerfilViewSet, basename='perfil')
router.register(r'experiencias', ExperienciaViewSet, basename='experiencia')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'reconocimientos', ReconocimientoViewSet, basename='reconocimiento')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'productos-laborales', ProductoLaboralViewSet, basename='producto-laboral')
router.register(r'productos-academicos', ProductoAcademicoViewSet, basename='producto-academico')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'ventas-garaje', VentaGarajeViewSet, basename='venta-garaje')

urlpatterns = [
    path('', include(router.urls)),
    path('cv-completo/', cv_completo, name='cv-completo'),
]