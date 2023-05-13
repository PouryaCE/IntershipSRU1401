from rest_framework import serializers
from accounts.models import School, Student, User


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ('slug', 'created', 'updated')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'phone_number', 'gender', 'student_id', 'field')


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'gender')
