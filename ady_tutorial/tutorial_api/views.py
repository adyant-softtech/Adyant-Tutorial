from multiprocessing import context
from django.shortcuts import render
from rest_framework import viewsets
from tutorial.models import Student
from tutorial_api.serializers import StudentSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from rest_framework.decorators import api_view, authentication_classes, permission_classes

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class GetStudentsById(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_id = request.GET.get('student_id')
        data = Student.objects.filter(student_id=student_id)
        serializers = StudentSerializer(data, many=True)
        return Response(serializers.data)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def GetStudentsByIds(request):
    student_id = request.GET.get('student_id')
    data = Student.objects.filter(student_id=student_id)
    serializers = StudentSerializer(data, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_auth_key(request):
    content = {
        'user': str(request.user),
        'auth': str(request.auth)
    }

    return Response(content)


class RegisterAPIView(APIView):

    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        register = Register.object.create()



