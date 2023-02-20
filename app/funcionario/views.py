from rest_framework import viewsets
from .models import Setor, Funcionario
from .serializer import SetorSerializer, FuncionarioSerializer


class FuncinarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer