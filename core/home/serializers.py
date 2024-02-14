from rest_framework import serializers
from home.models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        # fields = ['name','age','father_name']
        exclude = ['id']
        # fields = '__all__'
