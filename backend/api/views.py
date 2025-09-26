from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
print("views.py-----------")
class Studentcl(generics.ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer
    print("Query---------------")
    print(queryset.query)

class StudentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer
    print("Query rud---------------")
    print(queryset.query)
