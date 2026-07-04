from django.urls import path
from api import views

urlpatterns = [
    path("employees/", views.employee_list, name="employee_list"),
    path("employee_detail/<int:id>/", views.employee_detail, name="employee_detail"),
    path("employee_add/", views.employee_add, name="employee_add"),
    path("employee_update/<int:id>/", views.employee_update, name="employee_update"),
    path("employee_delete/<int:id>/", views.employee_delete, name="employee_delete"),
]
