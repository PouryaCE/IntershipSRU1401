from rest_framework import serializers
from accounts.models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ('slug', 'created', 'updated')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'phone_number', 'gender', 'student_id', 'field')

