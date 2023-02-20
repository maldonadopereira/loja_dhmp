from django.db import models
from app.core.models import TimeStampedModel


class Venda(TimeStampedModel):
    funcionario = models.ForeignKey('funcionario.Funcionario', on_delete=models.CASCADE)
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return f'Venda de: {self.nome}'

class VendaProdutos(TimeStampedModel):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey('produto.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(null=False, default=1)

    class Meta:
        verbose_name = 'Produto da Venda'
        verbose_name_plural = 'Produtos da Venda'

    def __str__(self):
        return self.venda
