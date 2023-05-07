from django.urls import path
from .views import ListSchool
app_name = 'official_manager'

urlpatterns = [
    path('list-school/<int:office_id>/', ListSchool.as_view(), name='list-school')
]