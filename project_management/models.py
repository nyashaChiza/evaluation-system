from django.db import models
from django.conf import settings
from django.shortcuts import reverse

STATUS_OPTIONS = settings.STATUS_OPTIONS

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=35, choices=STATUS_OPTIONS)
    description = models.CharField(max_length=255)
    project_owner = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):    
        return reverse('list-projects')
    