from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - by ' + self.user.username


# ==================== MODELOS PARA EL CV ====================

class Perfil(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Experiencia(models.Model):
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    inicio = models.DateField()
    fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencias Laborales'
        ordering = ['-inicio']

    def __str__(self):
        return f"{self.puesto} - {self.empresa}"


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    inicio = models.DateField()
    duracion = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-inicio']

    def __str__(self):
        return self.nombre


class Reconocimiento(models.Model):
    titulo = models.CharField(max_length=200)
    otorgado = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nombre


class ProductoLaboral(models.Model):
    nombre = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    inicio = models.DateField()
    fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tecnologias = models.TextField(blank=True, null=True)
    rol = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-inicio']

    def __str__(self):
        return self.nombre


class ProductoAcademico(models.Model):
    tipo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=300)
    institucion = models.CharField(max_length=200)
    fecha = models.DateField()
    autores = models.TextField(blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    palabras = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


class VentaGaraje(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    imagen = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL de la imagen")
    estado = models.CharField(max_length=50, choices=[
        ('nuevo', 'Nuevo'),
        ('como_nuevo', 'Como nuevo'),
        ('usado_bueno', 'Usado - Buen estado'),
        ('usado_regular', 'Usado - Regular'),
    ], default='usado_bueno', verbose_name="Estado")
    categoria = models.CharField(max_length=100, blank=True, verbose_name="Categoría")
    vendido = models.BooleanField(default=False, verbose_name="¿Vendido?")
    fecha_publicacion = models.DateField(auto_now_add=True, verbose_name="Fecha de publicación")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Venta de Garaje"
        verbose_name_plural = "Ventas de Garaje"
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"