
from django.urls import path

from project_management.views import (ProjectCreateView, ProjectDeleteView,
                    ProjectDetailView, ProjectListView,
                    ProjectUpdateView)


urlpatterns = [
    path("index/", ProjectListView.as_view(), name="list-projects"),
    path("create/", ProjectCreateView.as_view(), name="create-department"),
    path("detail/<int:pk>/",ProjectDetailView.as_view(),name="detail-project"),
    path("update/<int:pk>/", ProjectUpdateView.as_view(), name="update-project"),
    path("delete/<int:pk>/", ProjectDeleteView.as_view(),name="delete-project"),
]