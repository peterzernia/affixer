from django.urls import path, include
from api.views import TransformationsListView


urlpatterns = [
    path('words/', TransformationsListView.as_view()),
]
