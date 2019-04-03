from django.urls import path, include
from api.views import TransformationsListView


urlpatterns = [
    path('transformations/', TransformationsListView.as_view()),
]
