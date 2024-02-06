from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import Student
from .serializers import StudentSerializer

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPIView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        id = request.GET.get('id')
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        try:
            python_data = JSONParser().parse(request)
            serializer = StudentSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Data created'}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except JSONParserError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    def put(self, request):
        try:
            python_data = JSONParser().parse(request)
            id = python_data.get('id')
            if id is not None:
                try:
                    stu = Student.objects.get(id=id)
                    serializer = StudentSerializer(stu, data=python_data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return JsonResponse({'msg': 'Data updated'})
                    return JsonResponse(serializer.errors, status=400)
                except Student.DoesNotExist:
                    return JsonResponse({'error': 'Student not found'}, status=404)
            return JsonResponse({'error': 'ID field is required'}, status=400)
        except JSONParserError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    def delete(self, request):
        try:
            python_data = JSONParser().parse(request)
            id = python_data.get('id')
            if id is not None:
                try:
                    stu = Student.objects.get(id=id)
                    stu.delete()
                    return JsonResponse({'msg': 'Data deleted'})
                except Student.DoesNotExist:
                    return JsonResponse({'error': 'Student not found'}, status=404)
            return JsonResponse({'error': 'ID field is required'}, status=400)
        except JSONParserError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)



