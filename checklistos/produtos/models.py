from django.db import models


class Produto(models.Model):
    nomelongo = models.CharField(max_length=80)
    preco = models.DecimalField(verbose_name='Preço', name='preco', max_digits=22, decimal_places=2)
    descricao = models.TextField(max_length=500)
    foto = models.ImageField(max_length=200, upload_to='produtos/', null=True)

    def __str__(self):
        return self.nomelongo

    def __repr__(self):
        return f'Produto(nomelongo={self.nomelongo!r}, preco={self.preco!r}, descricao={self.descricao!r}'
