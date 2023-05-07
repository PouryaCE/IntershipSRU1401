from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import School, OfficeManager
from .serializers import SchoolSerializer
from rest_framework import status
# Create your views here.
from ..reports.models import Request
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

    def post(self, request, office_id,school_id):
        school = School.objects.get(pk=school_id)
        manager = school.manager
        text = "Do you want to have student as inter ship?"
        Request.objects.create(manager=manager , text=text)
        messages.success(request, "request sent to manager successfully", 'success')
        return reverse_lazy('office_manager:list_school')




