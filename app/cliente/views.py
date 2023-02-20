from django.http import Http404
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Cliente, Endereco
from .serializer import ClienteSerializer, EnderecoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

'''class ClienteList(APIView):
    def get(self, request):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteMethodObject(APIView):
    def get_object(self, id):
        try:
            return Cliente.objects.get(id)
        except:
            raise Http404

    def get(self, request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente, data=request.data)
        return Response(serializer.data)
'''