from rest_framework import serializers

from . models import *

#convert model object into json 

class studentSerializer(serializers.ModelSerializer):
    print("serializers.py----------")
    class Meta:
        model=student
        fields='__all__'