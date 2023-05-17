from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from reports.models import Request
from accounts.models import School


class ShowRequest(APIView):
    def get(self, request, school_id):
        school = School.objects.get(pk=school_id)
        my_request = Request.objects.filter(school=school)
        request_texts = [req.text for req in my_request]
        return Response({'texts': request_texts})


class AcceptRequest(APIView):
    def post(self, request, school_id):
        capacity = request.POST.get('capacity')
        school = School.objects.get(pk=school_id)
        # and request.user == school.manager in bayad add beshe
        if school.capacity == 0 and request.user == school.manager:
            school.capacity = capacity
            school.save()
            return Response({'message': 'success'})
        return Response({'message': 'error'})


