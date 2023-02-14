from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from project_management.models import Project
from project_management.forms.createForm import ProjectForm


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/index.html'
    

class ProjectCreateView(CreateView):
    model = Project
    formclass = ProjectForm
    template_name = 'projects/create.html'
    
    
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/update.html'
        
        
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/update.html'
    

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/update.html'