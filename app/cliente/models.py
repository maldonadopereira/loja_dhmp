from django.db import models
from app.core.models import TimeStampedModel


class Endereco(TimeStampedModel):
    UF_CHOICE = [
        ['AC', 'Acre'],
        ['AL', 'Alagoas'],
        ['AP', 'Amapá'],
        ['AM', 'Amazonas'],
        ['BA', 'Bahia'],
        ['CE', 'Ceará'],
        ['ES', 'Espírito Santo'],
        ['GO', 'Goiás'],
        ['MA', 'Maranhão'],
        ['MT', 'Mato Grosso'],
        ['MS', 'Mato Grosso do Sul'],
        ['MG', 'Minas Gerais'],
        ['PA', 'Pará'],
        ['PB', 'Paraíba'],
        ['PR', 'Paraná'],
        ['PE', 'Pernambuco'],
        ['PI', 'Piauí'],
        ['RJ', 'Rio de Janeiro'],
        ['RN', 'Rio Grande do Norte'],
        ['RS', 'Rio Grande do Sul'],
        ['RO', 'Rondônia'],
        ['RR', 'Roraima'],
        ['SC', 'Santa Catarina'],
        ['SP', 'São Paulo'],
        ['SE', 'Sergipe'],
        ['TO', 'Tocantins'],
        ['DF', 'Distrito Federal'],
    ]
    endereco = models.CharField('Endereço', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    uf = models.CharField('Estado', max_length=2, choices=UF_CHOICE)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.endereco

class Cliente(TimeStampedModel):
    SEXO_CHOICE = [
        ['M', 'Masculino'],
        ['F', 'Feminino'],
    ]
    TIPO_CHOICE = [
        ['PF', 'Pessoa Física'],
        ['PJ', 'Pessoa Jurídica'],
    ]

    nome = models.CharField('Nome',max_length=100)
    sexo = models.CharField('Sexo',max_length=1, choices=SEXO_CHOICE)
    data_nascimento = models.DateField('Data de Nascimento', auto_now=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField('Telefone', max_length=25)
    tipo = models.CharField('Tipo',max_length=2, choices=TIPO_CHOICE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
