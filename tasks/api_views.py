from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Task, Perfil, Experiencia, Curso,
    Reconocimiento, Producto, ProductoLaboral, ProductoAcademico
)
from .serializers import (
    TaskSerializer, PerfilSerializer, ExperienciaSerializer,
    CursoSerializer, ReconocimientoSerializer, ProductoSerializer,
    ProductoLaboralSerializer, ProductoAcademicoSerializer
)


# ViewSets para cada modelo (CRUD completo)
class PerfilViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver perfiles
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class ExperienciaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver experiencias laborales
    """
    queryset = Experiencia.objects.all().order_by('-inicio')
    serializer_class = ExperienciaSerializer


class CursoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver cursos
    """
    queryset = Curso.objects.all().order_by('-inicio')
    serializer_class = CursoSerializer


class ReconocimientoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver reconocimientos
    """
    queryset = Reconocimiento.objects.all().order_by('-fecha')
    serializer_class = ReconocimientoSerializer


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver productos
    """
    queryset = Producto.objects.all().order_by('-created_at')
    serializer_class = ProductoSerializer


class ProductoLaboralViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver productos laborales
    """
    queryset = ProductoLaboral.objects.all().order_by('-inicio')
    serializer_class = ProductoLaboralSerializer


class ProductoAcademicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver productos académicos
    """
    queryset = ProductoAcademico.objects.all().order_by('-fecha')
    serializer_class = ProductoAcademicoSerializer


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver tareas
    """
    queryset = Task.objects.all().order_by('-created')
    serializer_class = TaskSerializer


# Vista especial para obtener todo el CV de una vez
@api_view(['GET'])
def cv_completo(request):
    """
    Devuelve todos los datos del CV en una sola respuesta
    """
    perfil = Perfil.objects.first()  # Obtener el primer (y único) perfil
    
    data = {
        'perfil': PerfilSerializer(perfil).data if perfil else None,
        'experiencias': ExperienciaSerializer(
            Experiencia.objects.all().order_by('-inicio'), 
            many=True
        ).data,
        'cursos': CursoSerializer(
            Curso.objects.all().order_by('-inicio'), 
            many=True
        ).data,
        'reconocimientos': ReconocimientoSerializer(
            Reconocimiento.objects.all().order_by('-fecha'), 
            many=True
        ).data,
        'productos': ProductoSerializer(
            Producto.objects.all().order_by('-created_at'), 
            many=True
        ).data,
        'productos_laborales': ProductoLaboralSerializer(
            ProductoLaboral.objects.all().order_by('-inicio'), 
            many=True
        ).data,
        'productos_academicos': ProductoAcademicoSerializer(
            ProductoAcademico.objects.all().order_by('-fecha'), 
            many=True
        ).data,
    }
    
    return Response(data)