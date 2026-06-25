from django.shortcuts import render
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def studentapi(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data)

    