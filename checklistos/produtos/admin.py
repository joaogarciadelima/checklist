from django.contrib import admin

from checklistos.produtos.models import Produto


@admin.register(Produto)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = 'nomelongo preco'.split()
    ordering = ('nomelongo',)
