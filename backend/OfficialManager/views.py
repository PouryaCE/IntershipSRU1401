from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import School, OfficeManager, Student
from .serializers import SchoolSerializer, StudentSerializer, ManagerSerializer
from rest_framework import status
# Create your views here.
from reports.models import Request, Request_Office
from django.contrib import messages
from django.urls import reverse_lazy


class ListSchool(APIView):
    def get(self, request, office_id):
        office_manager = OfficeManager.objects.get(pk=office_id)
        schools = School.objects.filter(office_manager=office_manager)
        ser_data = SchoolSerializer(instance=schools, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)


class AddSchool(APIView):
    def get(self, request, office_id):
        office_manager = OfficeManager.objects.get(pk=office_id)
        schools = School.objects.filter(office_manager=office_manager, capacity=0)
        ser_data = SchoolSerializer(instance=schools, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)

    def post(self, request, office_id, school_id):
        school = School.objects.get(pk=school_id)
        manager = school.manager
        text = "Do you want to have student as inter ship?"
        if Request.objects.filter(manager=manager, text=text).exists() and school.capacity > 0:
            messages.error(request, "request has been send to the manager before", 'error')
            return Response({"message": "error"})
        Request.objects.create(manager=manager, text=text)
        messages.success(request, "request sent to manager successfully", 'success')
        return Response({"message": "success"})


class AddInterShip(APIView):
    def get(self, request, office_id, student_id):
        office_manager = OfficeManager.objects.get(pk=office_id)
        schools = School.objects.filter(office_manager=office_manager, capacity__gt=0)
        ser_data = SchoolSerializer(instance=schools, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)

    def post(self, request, office_id, student_id, school_id):
        student = Student.objects.get(pk=student_id)
        school = School.objects.get(pk=school_id)
        office_manager = OfficeManager.objects.get(pk=office_id)
        if school.capacity > 0 and school.office_manager == office_manager and student.school2 is None:
            school.capacity = school.capacity - 1
            school.save()
            student.school2 = school
            student.save()
            request_student = Request_Office.objects.filter(student=student)
            request_student.delete()
            return Response({"message": "success"})
        return Response({"message": "error"})


#the request from student to office manager

class ShowRequest(APIView):
    def get(self,request,office_id):
        office_manager = OfficeManager.objects.get(pk=office_id)
        request_office = Request_Office.objects.filter(office_manager=office_manager)
        students = [request.student for request in request_office]
        ser_data = StudentSerializer(instance=students, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)


#the request from office manager to school manager

class MyRequest(APIView):
    def get(self, request, office_id):
        office_manager = OfficeManager.objects.get(pk=office_id)
        school_request = Request.objects.filter(school__office_manager=office_manager)
        manager = [request.school.manager for request in school_request]
        ser_data = ManagerSerializer(instance=manager, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)

