from django.urls import path, include
from rest_framework import routers
from . import views
from app.cliente.views import ClienteViewSet, EnderecoViewSet
from app.funcionario.views import SetorViewSet, FuncinarioViewSet
from app.produto.views import CategoriaViewSet, ProdutoViewSet
from app.venda.views import VendaViewSet, VendaProdutosViewSet

app_name = 'core'
router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet, basename='Clientes')
router.register('endereco', EnderecoViewSet, basename='Enderecos')
router.register('setor', SetorViewSet, basename='Setor')
router.register('funcionario', FuncinarioViewSet, basename='Funcionario')
router.register('categoria', CategoriaViewSet, basename='Categoria')
router.register('produto', ProdutoViewSet, basename='Produto')
router.register('venda', VendaViewSet, basename='Venda')
router.register('vendaproduto', VendaProdutosViewSet, basename='VendaProduto')

urlpatterns = [
    path('', include(router.urls)),
    ]
