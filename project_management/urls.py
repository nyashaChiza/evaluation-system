
from django.urls import path

from project_management.views import (ProjectCreateView, ProjectDeleteView,
                    ProjectDetailView, ProjectListView,ProjectCategoriesView,
                    ProjectUpdateView, ProjectQuestionsView, ProjectAnswersView, ProjectInsightsView)


urlpatterns = [
    path("index/", ProjectListView.as_view(), name="list-projects"),
    path("create/", ProjectCreateView.as_view(), name="create-project"),
    path("details/<int:pk>/",ProjectDetailView.as_view(),name="project-detail"),
    path("delete/<int:pk>/", ProjectDeleteView.as_view(),name="delete-project"),
    path("details/categories/<int:pk>/",ProjectCategoriesView.as_view(),name="project-categories"),
    path("details/questions/<int:pk>/",ProjectQuestionsView.as_view(),name="project-questions"),
    path("details/answers/<int:pk>/",ProjectAnswersView.as_view(),name="project-answers"),
    path("details/insights/<int:pk>/",ProjectInsightsView.as_view(),name="project-insights"),
    path("update/<int:pk>/", ProjectUpdateView.as_view(), name="update-project"),
]