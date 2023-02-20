from rest_framework import viewsets
from .models import Venda, VendaProdutos
from .serializer import VendaSerializer, VendaProdutosSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaProdutosViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaProdutosSerializer