from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')
    list_display_links = ('id', 'nome', 'email')
