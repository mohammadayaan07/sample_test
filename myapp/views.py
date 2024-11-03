from django.shortcuts import render,HttpResponse
from .serializers import StudentSerializer
from .models import student
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
# Create your views here.

def student_views(request):
    stu=student.objects.all() #geting  the data
    stu_serializer=StudentSerializer(stu,many=True) #converting into py data
    json_data=JSONRenderer().render(stu_serializer.data) #converting insto json
    return HttpResponse(json_data,content_type='application/json')
    
def student_id(request,pk):
    stu=student.objects.get(rollno=pk) #
    stu_serializer=StudentSerializer(stu)
    #json_data=JSONRenderer().render(stu_serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    # we will use the jsonrespone where we dont need to are converting json data it will auto taked
    return JsonResponse(stu_serializer.data)