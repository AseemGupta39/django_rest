from rest_framework import serializers
from home.models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        # fields = ['name','age','father_name']
        # exclude = ['id']
        fields = '__all__'
    
    def validate(self,data):
        
        if data['age']  < 18:
            raise serializers.ValidationError({'error':'age cannot be less than 18'}) 
    
        num_arr = "123456789".split()
        for ch in data['name']:
            if ch.isdigit():
               raise serializers.ValidationError({'error':'name cannot be contain numbers'})    
            
        return data
    
