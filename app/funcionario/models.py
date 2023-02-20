from django.db import models
from app.core.models import TimeStampedModel


class Setor(TimeStampedModel):
    TIPO_CHOICES = [
        ['Vendas Internas', 'Vendas Internas'],
        ['Vendas Externas', 'Vendas Externas']
    ]
    nome = models.CharField('Setor', max_length=50)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO_CHOICES)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.nome


class Funcionario(TimeStampedModel):
    cpf = models.PositiveIntegerField()
    data_nascimento = models.DateField('Data de Nascimento', auto_now=False)
    nome = models.CharField('Nome', max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome