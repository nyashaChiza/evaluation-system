from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from category_management.models import Category
from category_management.forms.category_form import CategoryForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories/index.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    
class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/create.html'
    success_message = 'Category Created Successfully'
    
    def get_success_url(self) -> str:
        return reverse('list-categories')

    
class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/update.html'
    success_message = 'Category Updated Successfully'
    
    def get_success_url(self) -> str:
        return reverse('list-categories')
        
        
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/details.html'


class CategoryDeleteView(SuccessMessageMixin,DeleteView):
    model = Category
    template_name = 'categories/update.html'
    success_message = 'Category Deleted Successfully'
    
    def get_success_url(self) -> str:
        return reverse('list-categories')