from django.urls import path
from rest_framework import routers


from .views import InterestViewset, TimelineItemListView


router = routers.DefaultRouter()

router.register('interests', InterestViewset, basename='interests')




app_name = 'user_api'
urlpatterns = [

    path('timeline/', TimelineItemListView.as_view(), name='timeline'),

] + router.urls