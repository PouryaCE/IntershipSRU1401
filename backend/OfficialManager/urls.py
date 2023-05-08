from django.urls import path
from .views import ListSchool, AddSchool, AddInterShip, ShowRequest
app_name = 'official_manager'

urlpatterns = [
    path('list-school/<int:office_id>/', ListSchool.as_view(), name='list-school'),
    path('add-school/<int:office_id>/', AddSchool.as_view(), name='add-get'),
    path('add-school/<int:office_id>/<int:school_id>/', AddSchool.as_view(), name='add-post'),
    path('add-intership/<int:office_id>/<int:student_id>/', AddInterShip.as_view(), name='inter_get'),
    path('add-intership/<int:office_id>/<int:student_id>/<int:school_id>/', AddInterShip.as_view(), name='inter-post'),
    path('student-request/<int:office_id>/',ShowRequest.as_view(), name='student_request')
]