from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from project_management.models import Project
from project_management.forms.createForm import ProjectForm
from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_projects'] = context['projects'].count()
        context['number_of_categories'] = context['projects'].count()
        context['number_of_questions'] = context['projects'].count()   
        return context
    

class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'
    success_message = 'Project Created Successfully'

    
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/update.html'
        
        
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/details.html'
    

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/update.html'