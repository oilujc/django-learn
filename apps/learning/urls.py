from django.urls import path

from .views import LearningView, InterestsView

app_name = 'learning'
urlpatterns = [
    path('interests/', InterestsView.as_view(), name='interests'),
    path('learn/', LearningView.as_view(), name='learning'),
]