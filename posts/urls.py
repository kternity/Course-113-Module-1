from django.urls import path
from .views import (
   PostListView,
   PostUpdateView,
   PostDelteView
)

urlpatterns = [
   path("", PostListView.as_view(), name="list"),
   path("<int:pk>/edit/", PostUpdateview.as_view(), name="edit"),
   path("<int:pk>/delete/", PostDelteView.as_view(), name="delete"),
]

#Try this before next class
# Create templates and urlpatterns for:
# PostListView
# PostDetailView
# PostCreateView