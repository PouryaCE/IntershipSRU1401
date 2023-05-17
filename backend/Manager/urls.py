from django.urls import path
from .views import ShowRequest, AcceptRequest
app_name = 'manager'
urlpatterns = [
    path('show-request/<int:school_id>/', ShowRequest.as_view(), name='my-request'),
    path('accept-request/<int:school_id>/', AcceptRequest.as_view(), name='accept'),


]
