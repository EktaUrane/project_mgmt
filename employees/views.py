from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Department, Project, Employee, EmployeeProject
from .serializers import UserSerializer, DepartmentSerializer, ProjectSerializer, EmployeeSerializer, EmployeeProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeProjectViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProject.objects.all()
    serializer_class = EmployeeProjectSerializer
