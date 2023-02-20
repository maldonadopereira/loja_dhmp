from django.db import models
from app.core.models import TimeStampedModel


class Categoria(TimeStampedModel):
    TIPO_CHOICES = [
        [1, 'Atacado'],
        [2, 'Varejo']
    ]
    nome = models.CharField('Categoria', max_length=50)
    tipo = models.IntegerField('Tipo', choices=TIPO_CHOICES)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Produto(TimeStampedModel):
    nome = models.CharField('Produto', max_length=200)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estoque = models.PositiveIntegerField('Estoque')
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome