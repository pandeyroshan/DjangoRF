from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import dataSet
from django.core import serializers
import json
# Create your views here.

class dataSetView(APIView):
    def get(self, request, format=None):
        data = dataSet.objects.all()
        json_data = serializers.serialize('json', data)
        print(json_data)
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