from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello from Django on Vercel 🚀</h1>")


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
