from django.db import models
from project_management.models import Project
from django.conf import settings

STATUS_OPTIONS = settings.STATUS_OPTIONS

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    project = models.ForeignKey(to=Project, on_delete=models.SET_NULL, blank=True, related_name='categories', null=True)
    status = models.CharField(max_length=35, choices=STATUS_OPTIONS, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
