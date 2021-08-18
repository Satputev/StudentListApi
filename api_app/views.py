from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api_app.models import Student,Attendance
from api_app.serializers import StudentSerializer,AttendenceSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students=Student.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'GET':
        student_serializer = StudentSerializer(student)
        return JsonResponse(student_serializer.data)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def attendance(request):
    if(request.method=='POST'):
        attendance = JSONParser().parse(request)
        attendance_serializer = AttendenceSerializer(data=attendance)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return JsonResponse(attendance_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        attendance=Attendance.objects.all()
        attendance_serializer = AttendenceSerializer(attendance, many=True)
        return JsonResponse(attendance_serializer.data, safe=False)




