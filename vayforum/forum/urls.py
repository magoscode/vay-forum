from django.urls import path
from .views import forum_view

urlpatterns = [
    path("", forum_view, name="forum"),
]
