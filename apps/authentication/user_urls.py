from django.urls import path

from .views import ProfileView, TimelineView


app_name = 'authentication_user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('timeline/', TimelineView.as_view(), name='timeline'),
]