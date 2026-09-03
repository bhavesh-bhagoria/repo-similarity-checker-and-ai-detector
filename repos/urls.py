from django.urls import path
from .views import RepoCreateView


urlpatterns = [
    path("repos/", RepoCreateView.as_view()),
]