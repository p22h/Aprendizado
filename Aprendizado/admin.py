from django.contrib import admin
from .models import Aprendizado, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Historico", { 'fields':('cursos_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Aprendizado)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
