from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeListSerializer, EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    # serializer_class = EmployeeSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return EmployeeListSerializer
        else:
            return EmployeeSerializer
