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


class PerfilViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar perfiles (CRUD completo)
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class ExperienciaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar experiencias (CRUD completo)
    """
    queryset = Experiencia.objects.all().order_by('-inicio')
    serializer_class = ExperienciaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar cursos (CRUD completo)
    """
    queryset = Curso.objects.all().order_by('-inicio')
    serializer_class = CursoSerializer


class ReconocimientoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar reconocimientos (CRUD completo)
    """
    queryset = Reconocimiento.objects.all().order_by('-fecha')
    serializer_class = ReconocimientoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar productos (CRUD completo)
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoLaboralViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar productos laborales (CRUD completo)
    """
    queryset = ProductoLaboral.objects.all().order_by('-inicio')
    serializer_class = ProductoLaboralSerializer


class ProductoAcademicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar productos académicos (CRUD completo)
    """
    queryset = ProductoAcademico.objects.all().order_by('-fecha')
    serializer_class = ProductoAcademicoSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar tareas (CRUD completo)
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class VentaGarajeViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar ventas de garaje (CRUD completo)
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