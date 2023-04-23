from django.urls import path

from .views import( 
    ActivityProgressListCreateView,
    LessonDetailView,
    LessonLikeCreateView,
    LessonLikeDeleteView,
    UserActivityDetailView,
    UserActivityListCreateView,
    UserActivityLikeCreateView,
    UserActivityLikeDeleteView,
    UserActivityRatingCreateView
)

app_name = 'learning-api'
urlpatterns = [
    path('activity-progress/', ActivityProgressListCreateView.as_view(), name='activity-progress'),
    path('lesson/<slug:slug>/', LessonDetailView.as_view(), name='lesson-detail'),

    path('lesson-like/', LessonLikeCreateView.as_view(), name='lesson-like'),
    path('lesson-like/<int:id>/', LessonLikeDeleteView.as_view(), name='lesson-like-delete'),

    path('user-activity/', UserActivityListCreateView.as_view(), name='user-activity'),
    path('user-activity/<slug:slug>/', UserActivityDetailView.as_view(), name='user-activity'),
    path('user-activity-like/', UserActivityLikeCreateView.as_view(), name='user-activity-like'),
    path('user-activity-like/<int:id>/', UserActivityLikeDeleteView.as_view(), name='user-activity-like-delete'),

    path('user-activity-rating/', UserActivityRatingCreateView.as_view(), name='user-activity-rating'),

]