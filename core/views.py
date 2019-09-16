from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import dataSet
from django.core import serializers
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.

@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    data = request.data
    username = data['username']
    password = data['password']
    user = authenticate(username=username,password=password)
    token = Token.objects.get_or_create(user=user)
    return Response({'Token': token[0].key})

class dataSetView(APIView):
    def get(self, request, format=None):
        data = dataSet.objects.all()
        json_data = serializers.serialize('json', data)
        print(request.user)
        return Response(json_data)
    def post(self, request, format=None):
        data = request.data
        dataID = data['dataID']
        data = data['data']
        data = dataSet.objects.create(dataID=dataID,data=data)
        data.save()
        return Response({'Message':'Saved'})
    def put(self, request, format=None):
        data = request.data
        dataID = data['dataID']
        data = data['data']
        obj = dataSet.objects.get(dataID=dataID)
        obj.data = data
        obj.save()
        return Response({'Message': 'Altered'})
    def delete(self,request, format=None):
        data = request.data
        dataID = data['dataID']
        dataSet.objects.get(dataID=dataID).delete()
        return Response({'Message':'Deleted'})
