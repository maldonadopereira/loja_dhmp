from rest_framework import serializers
from .models import Venda, VendaProdutos

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

class VendaProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaProdutos
        fields = '__all__'