from .models import Receita
from django.contrib import admin

@admin.register(Receita)
class ListandoReceitas(admin.ModelAdmin):
    list_display = ['id', 'nome_receita', 'data_receita', 'publicada', 'tempo_preparo']
    list_display_links = ('nome_receita', 'id')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 20



