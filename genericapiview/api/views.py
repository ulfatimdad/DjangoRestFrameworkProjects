from rest_framework import generics, mixins
from api.models import Employee
from api.serializer import EmployeeListSerializer, EmployeeSerializer


class StudenListCreateAPI(
    generics.GenericAPIView,  # DRF base class where we define queryset and serializer
    mixins.ListModelMixin,  # DRF prebuild classes where crud operation logic is available
    mixins.CreateModelMixin,
):
    queryset = Employee.objects.all()

    # serializer_class = EmployeeListSerializer
    # serializer_class = EmployeeSerializer
    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeListSerializer
        return EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetriveUpdateDeleteAPI(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
