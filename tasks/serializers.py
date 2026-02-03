from rest_framework import serializers
from .models import (
    Task, Perfil, Experiencia, Curso, 
    Reconocimiento, Producto, ProductoLaboral, ProductoAcademico
)


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'


class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class ReconocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reconocimiento
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoLaboral
        fields = '__all__'


class ProductoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoAcademico
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'