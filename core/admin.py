from django.contrib import admin
from .models import GeneroJogo, Jogo
# Register your models here.

class Jogos(admin.ModelAdmin):
    list_display=('nomeJogo', 'person', 'generoJogo', 'ano')
    search_fields=('nome')

admin.site.register(Jogo)
admin.site.register(GeneroJogo)

