from django.contrib import admin
from .models import Task, Perfil, Experiencia, Curso, Reconocimiento, Producto, ProductoLaboral, ProductoAcademico

# Configuración para Task (tu modelo original)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'done', 'created')
    list_filter = ('done', 'created')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)

# Configuración para Perfil
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'ciudad')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('ciudad',)

admin.site.register(Perfil, PerfilAdmin)

# Configuración para Experiencia
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'cargo', 'fecha_inicio', 'fecha_fin', 'perfil')
    list_filter = ('fecha_inicio', 'fecha_fin')
    search_fields = ('empresa', 'cargo', 'descripcion')
    readonly_fields = ('perfil',)

admin.site.register(Experiencia, ExperienciaAdmin)

# Configuración para Curso
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'fecha_finalizacion', 'perfil')
    list_filter = ('fecha_finalizacion',)
    search_fields = ('nombre', 'institucion')
    readonly_fields = ('perfil',)

admin.site.register(Curso, CursoAdmin)

# Configuración para Reconocimiento
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'otorgado_por', 'fecha', 'perfil')
    list_filter = ('fecha',)
    search_fields = ('titulo', 'otorgado_por', 'descripcion')
    readonly_fields = ('perfil',)

admin.site.register(Reconocimiento, ReconocimientoAdmin)

# Configuración para Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha', 'perfil')
    list_filter = ('tipo', 'fecha')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('perfil',)

admin.site.register(Producto, ProductoAdmin)

# Configuración para ProductoLaboral
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('producto', 'empresa', 'rol')
    search_fields = ('empresa', 'rol', 'tecnologias_utilizadas')
    readonly_fields = ('producto',)

admin.site.register(ProductoLaboral, ProductoLaboralAdmin)

# Configuración para ProductoAcademico
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'institucion', 'programa')
    search_fields = ('institucion', 'programa', 'asesor')
    readonly_fields = ('producto',)

admin.site.register(ProductoAcademico, ProductoAcademicoAdmin)