from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.models import Employee
from api.serializer import EmployeeSerializer, EmployeeListSerializer


@api_view(["GET"])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeListSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def employee_detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist as e:
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


@api_view(["POST"])
def employee_add(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(data=request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH", "PUT"])
def employee_update(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist as e:
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = EmployeeSerializer(employee, data=request.data)
    else:
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(request.data, status=status.HTTP_200_OK)

    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def employee_delete(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist as e:
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    employee.delete()
    return Response({"Deleted": True}, status=status.HTTP_200_OK)
