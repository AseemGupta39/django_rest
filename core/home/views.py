# from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Student
from home.serializers import StudentSerializer
# Create your views here. 

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs,many = True)
    return Response({'status':200,'payload':serializer.data})


@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)

    if request.data['age'] < 18:
        return Response({'status':403,'message':'age must begreater than 18'})

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403,'error':serializer.errors,'message':'Something went wrong'})
    
    serializer.save()    

    # print(data)
    return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})
