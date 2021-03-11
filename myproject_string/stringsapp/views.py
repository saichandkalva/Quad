from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from stringsapp.models import phonenum
import re
import json
from stringsapp.models import inputstring
# Create your views here.
from stringsapp.serializers import UserSerializer
from stringsapp.serializers import StringSerializer
from collections import OrderedDict


@api_view(['GET', 'POST'])
def phonenumbers(request):
    """

    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        phonenumbers = phonenum.objects.all()
        serializer = UserSerializer(phonenumbers, many=True)
        print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = extract_numbers(request.data['source'])
        return Response(data, status=status.HTTP_201_CREATED)

def extract_numbers(source):
    data=[]
    for i in re.findall(r'\+[-()\s\d]+?(?=\s*[+<])', source):
        od = OrderedDict()
        od["number"]=i
        data.append(od)
    serializer = UserSerializer(data=data,many=True)
    if serializer.is_valid():
        serializer.save()
    return data


