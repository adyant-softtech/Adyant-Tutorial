
from django.contrib.auth.models import User
from rest_framework import serializers

from tutorial.models import Student

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'stu_name', 'stu_class', 'stu_branch', 'address']