from rest_framework import serializers
from .models import (
    Task, Perfil, Experiencia, Curso, 
    Reconocimiento, Producto, ProductoLaboral, ProductoAcademico, VentaGaraje
)


class PerfilSerializer(serializers.ModelSerializer):
    ubicacion = serializers.SerializerMethodField()
    resumen_profesional = serializers.SerializerMethodField()
    linkedin = serializers.SerializerMethodField()
    github = serializers.SerializerMethodField()
    sitio_web = serializers.SerializerMethodField()
    
    class Meta:
        model = Perfil
        fields = '__all__'
    
    def get_ubicacion(self, obj):
        if obj.ciudad and obj.pais:
            return f"{obj.ciudad}, {obj.pais}"
        return obj.ciudad or obj.pais or "N/A"
    
    def get_resumen_profesional(self, obj):
        return obj.titulo or ""
    
    def get_linkedin(self, obj):
        return ""
    
    def get_github(self, obj):
        return ""
    
    def get_sitio_web(self, obj):
        return ""


class ExperienciaSerializer(serializers.ModelSerializer):
    cargo = serializers.CharField(source='puesto')
    fecha_inicio = serializers.DateField(source='inicio')
    fecha_fin = serializers.DateField(source='fin', allow_null=True)
    
    class Meta:
        model = Experiencia
        fields = ['id', 'cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'descripcion']


class CursoSerializer(serializers.ModelSerializer):
    fecha_finalizacion = serializers.DateField(source='inicio')
    certificado_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'institucion', 'fecha_finalizacion', 'certificado_url', 'imagen']
    
    def get_certificado_url(self, obj):
        return obj.imagen or ""


class ReconocimientoSerializer(serializers.ModelSerializer):
    organizacion = serializers.CharField(source='otorgado')
    titulo = serializers.CharField(source='titulo')
    
    class Meta:
        model = Reconocimiento
        fields = ['id', 'titulo', 'organizacion', 'fecha', 'descripcion', 'imagen']


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoLaboralSerializer(serializers.ModelSerializer):
    fecha = serializers.DateField(source='inicio')
    
    class Meta:
        model = ProductoLaboral
        fields = ['id', 'nombre', 'empresa', 'fecha', 'descripcion', 'tecnologias', 'rol', 'url', 'imagen']


class ProductoAcademicoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='titulo')
    
    class Meta:
        model = ProductoAcademico
        fields = ['id', 'tipo', 'nombre', 'institucion', 'fecha', 'autores', 'resumen', 'palabras', 'url', 'imagen']


class VentaGarajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaGaraje
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'