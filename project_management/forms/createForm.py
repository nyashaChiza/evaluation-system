from django.forms import ModelForm
from project_management.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude  = [ 'created', 'updated']
        fields = "__all__"
        
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs["class"] = "form-select js-select2"