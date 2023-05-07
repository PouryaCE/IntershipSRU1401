from rest_framework import serializers
from accounts.models import School
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ('slug','created','updated')