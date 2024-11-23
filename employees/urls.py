# employees/urls.py
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'employee-projects', views.EmployeeProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
