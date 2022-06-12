from django.contrib import admin

from django.contrib import admin
from petsy.models import Accesorio, Categoria,Cliente

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Accesorio)
admin.site.register(Cliente)