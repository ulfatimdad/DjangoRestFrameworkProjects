from django.urls import path
from api.views import StudentAPI

urlpatterns = [
    path("employees/", StudentAPI.as_view()),
    path("employees/<int:id>/", StudentAPI.as_view()),
    # path("employee_detail/<int:id>/", views.employee_detail, name="employee_detail"),
    # path("employee_add/", views.employee_add, name="employee_add"),
    # path("employee_update/<int:id>/", views.employee_update, name="employee_update"),
    # path("employee_delete/<int:id>/", views.employee_delete, name="employee_delete"),
]
