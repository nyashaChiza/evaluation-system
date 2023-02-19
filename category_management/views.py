from django.shortcuts import render
from django.views.generic import ListView
from category_management.models import Category

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category/index.html'