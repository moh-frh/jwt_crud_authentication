from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.permissions import IsAuthenticated

class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]