from django.contrib import admin
from .models import Autor, Tutoriais

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')


class TutoriaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo', 'data', 'imagem', 'conteudo', 'autor')


admin.site.register(Autor, AutorAdmin)
admin.site.register(Tutoriais, TutoriaisAdmin)
