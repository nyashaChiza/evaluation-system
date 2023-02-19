from django.db import models
from project_management.models import Project

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    project = models.OneToOneField(to=Project, on_delete=models.SET_NULL, blank=True, related_name='categories')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
