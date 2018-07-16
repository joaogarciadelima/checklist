from django.contrib import admin

from checklistos.servicos.models import Servico


@admin.register(Servico)
class ServicosAdmin(admin.ModelAdmin):
    list_display = 'nomelongo preco'.split()
    ordering = ('nomelongo',)
