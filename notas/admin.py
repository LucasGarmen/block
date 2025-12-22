from django.contrib import admin
from .models import Notas

@admin.register(Notas)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido_corto', 'fecha')

    def contenido_corto(self,obj):
        return obj.contenido[:10] + ('...' if len(obj.contenido)>10 else'')
    
    contenido_corto.short_description = 'Contenido'   