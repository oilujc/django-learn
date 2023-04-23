from django.urls import path

from .views import  ExploreView


app_name = 'explore'

urlpatterns = [
    path('', ExploreView.as_view(), name='explore'),
]