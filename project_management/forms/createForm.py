from django.forms import ModelForm
from project_management.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude  = ['status', 'created', 'updated']
        
        
        