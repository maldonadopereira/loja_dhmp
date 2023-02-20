# Generated by Django 4.1.7 on 2023-02-20 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('nome', models.CharField(max_length=50, verbose_name='Setor')),
                ('tipo', models.CharField(choices=[['Vendas Internas', 'Vendas Internas'], ['Vendas Externas', 'Vendas Externas']], max_length=20, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('cpf', models.PositiveIntegerField()),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.setor')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
