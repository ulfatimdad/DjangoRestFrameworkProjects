from django.urls import path
from api.views import StudenListCreateAPI, StudentRetriveUpdateDeleteAPI

urlpatterns = [
    path("employees/", StudenListCreateAPI.as_view()),
    path("employee/<int:pk>", StudentRetriveUpdateDeleteAPI.as_view()),
]
