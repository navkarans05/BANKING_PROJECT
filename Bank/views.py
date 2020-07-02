from django.shortcuts import render, redirect
from .serializers import detailSerializer,ifscSerializer
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,get_object_or_404

from rest_framework.parsers import JSONParser
from .models import detail
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import DetailForm




@api_view(['GET','POST'])
def detail_list(request):
    if request.method == 'GET':
        dtl=detail.objects.all()
        serializer=detailSerializer(dtl,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=detailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#---------------------------------------------------------------------
@api_view(['GET'])
def ifsc_list(request):
    if request.method == 'GET':
        dtl=detail.objects.all()
        serializer=ifscSerializer(dtl,many=True)
        return Response(serializer.data)
