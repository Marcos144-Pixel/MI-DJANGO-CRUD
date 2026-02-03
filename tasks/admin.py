from django.contrib import admin
from .models import Task, Perfil, Experiencia, Curso, Reconocimiento, Producto, ProductoLaboral, ProductoAcademico

# Configuración para Task (tu modelo original)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'user', 'important', 'done', 'created')
    list_filter = ('important', 'created')
    search_fields = ('title', 'description')
    
    def done(self, obj):
        return obj.datecompleted is not None
    done.boolean = True
    done.short_description = 'Completada'

admin.site.register(Task, TaskAdmin)


# Configuración para Perfil
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'email', 'telefono', 'ciudad', 'pais')
    search_fields = ('nombres', 'apellidos', 'email', 'ciudad')
    list_filter = ('ciudad', 'pais', 'estado_civil')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombres', 'apellidos', 'fecha_nacimiento', 'estado_civil')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'ciudad', 'pais')
        }),
        ('Profesional', {
            'fields': ('titulo',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Perfil, PerfilAdmin)


# Configuración para Experiencia
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('puesto', 'empresa', 'inicio', 'fin', 'esta_activo')
    list_filter = ('inicio', 'fin', 'empresa')
    search_fields = ('puesto', 'empresa', 'descripcion')
    readonly_fields = ('created_at',)
    date_hierarchy = 'inicio'
    
    def esta_activo(self, obj):
        return obj.fin is None
    esta_activo.boolean = True
    esta_activo.short_description = 'Actual'

admin.site.register(Experiencia, ExperienciaAdmin)


# Configuración para Curso
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'inicio', 'duracion')
    list_filter = ('inicio', 'institucion')
    search_fields = ('nombre', 'institucion')
    readonly_fields = ('created_at',)
    date_hierarchy = 'inicio'

admin.site.register(Curso, CursoAdmin)


# Configuración para Reconocimiento
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'otorgado', 'fecha')
    list_filter = ('fecha', 'otorgado')
    search_fields = ('titulo', 'otorgado', 'descripcion')
    readonly_fields = ('created_at',)
    date_hierarchy = 'fecha'

admin.site.register(Reconocimiento, ReconocimientoAdmin)


# Configuración para Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad', 'estado', 'created_at')
    list_filter = ('estado', 'created_at')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('created_at',)
    list_editable = ('precio', 'cantidad', 'estado')

admin.site.register(Producto, ProductoAdmin)


# Configuración para ProductoLaboral
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'rol', 'inicio', 'fin', 'esta_activo')
    list_filter = ('inicio', 'fin', 'empresa')
    search_fields = ('nombre', 'empresa', 'rol', 'descripcion', 'tecnologias')
    readonly_fields = ('created_at',)
    date_hierarchy = 'inicio'
    
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'empresa', 'rol')
        }),
        ('Fechas', {
            'fields': ('inicio', 'fin')
        }),
        ('Detalles', {
            'fields': ('descripcion', 'tecnologias', 'url', 'imagen')
        }),
        ('Sistema', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def esta_activo(self, obj):
        return obj.fin is None
    esta_activo.boolean = True
    esta_activo.short_description = 'Activo'

admin.site.register(ProductoLaboral, ProductoLaboralAdmin)


# Configuración para ProductoAcademico
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'institucion', 'fecha')
    list_filter = ('tipo', 'fecha', 'institucion')
    search_fields = ('titulo', 'institucion', 'autores', 'resumen', 'palabras')
    readonly_fields = ('created_at',)
    date_hierarchy = 'fecha'
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('tipo', 'titulo', 'institucion', 'fecha')
        }),
        ('Contenido', {
            'fields': ('autores', 'resumen', 'palabras')
        }),
        ('Enlaces y Multimedia', {
            'fields': ('url', 'imagen')
        }),
        ('Sistema', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(ProductoAcademico, ProductoAcademicoAdmin)