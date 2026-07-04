from rest_framework import serializers

from api.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ("name",)
