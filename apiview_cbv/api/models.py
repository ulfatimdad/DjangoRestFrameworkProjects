from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    dof = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
