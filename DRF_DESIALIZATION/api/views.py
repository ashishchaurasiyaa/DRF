from django.shortcuts import render
from .models import Student
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests


# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            res = {'msg': 'Invalid data provided'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json', status=400)
    else:
        res = {'msg': 'Method Not Allowed'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json', status=405)
