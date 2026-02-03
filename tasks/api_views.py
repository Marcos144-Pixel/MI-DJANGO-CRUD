from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Task, Perfil, Experiencia, Curso,
    Reconocimiento, Producto, ProductoLaboral, ProductoAcademico, VentaGaraje
)
from .serializers import (
    TaskSerializer, PerfilSerializer, ExperienciaSerializer,
    CursoSerializer, ReconocimientoSerializer, ProductoSerializer,
    ProductoLaboralSerializer, ProductoAcademicoSerializer, VentaGarajeSerializer
)


class PerfilViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver perfiles
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class ExperienciaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver experiencias
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
    queryset = Producto.objects.all()
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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class VentaGarajeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver ventas de garaje
    """
    queryset = VentaGaraje.objects.all().order_by('-fecha_publicacion')
    serializer_class = VentaGarajeSerializer


@api_view(['GET'])
def cv_completo(request):
    """
    Endpoint que devuelve todos los datos del CV en una sola respuesta
    """
    try:
        perfil = Perfil.objects.first()
        
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
                Producto.objects.all(), 
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
            'ventas_garaje': VentaGarajeSerializer(
                VentaGaraje.objects.all().order_by('-fecha_publicacion'),
                many=True
            ).data,
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )