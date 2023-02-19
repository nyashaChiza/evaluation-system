
from django.urls import path

from category_management.views import (CategoryCreateView, CategoryDeleteView,
                    CategoryDetailView, CategoryListView,CategoryCategoriesView,
                    CategoryUpdateView, CategoryQuestionsView, CategoryAnswersView, CategoryInsightsView)


urlpatterns = [
    path("index/", CategoryListView.as_view(), name="list-ctegories"),
    path("create/", CategoryCreateView.as_view(), name="create-category"),
    path("details/<int:pk>/",CategoryDetailView.as_view(),name="category-detail"),
    path("delete/<int:pk>/", CategoryDeleteView.as_view(),name="delete-category"),
    path("details/categories/<int:pk>/",CategoryCategoriesView.as_view(),name="category-categories"),
    path("details/questions/<int:pk>/",CategoryQuestionsView.as_view(),name="category-questions"),
    path("details/answers/<int:pk>/",CategoryAnswersView.as_view(),name="category-answers"),
    path("details/insights/<int:pk>/",CategoryInsightsView.as_view(),name="category-insights"),
    path("update/<int:pk>/", CategoryUpdateView.as_view(), name="update-category"),
]