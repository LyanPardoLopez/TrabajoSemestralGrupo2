from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from core.models import Tatuador
from .serializers import TatuadorSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_tatuadores(request):

    if request.method == 'GET':
        tatuador = Tatuador.objects.all()
        serializers = TatuadorSerializer(tatuador,many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializers=TatuadorSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_tatuador(request,id):
    try:
        tatuador=Tatuador.objects.get(idTatuador=id)
    except Tatuador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers=TatuadorSerializer(tatuador)
        return Response(serializers.data)
    if request.method == 'PUT' :
        data=JSONParser.parse(request)
        serializers=TatuadorSerializer(tatuador,data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers._data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        tatuador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        