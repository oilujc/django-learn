from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import (
    ActivityProgress,
    Lesson,
    LessonLike,
    UserActivity,
    UserActivityLike,
    UserActivityRating
)

from apps.learning.api.serializers import (
    ActivityProgressSerializer, 
    LessonSerializer, 
    LessonLikeSerializer, 
    UserActivitySerializer,
    UserActivityLikeSerializer,
    UserActivityRatingSerializer
)


from apps.learning.services.activity_progress_service import ActivityProgresService
from apps.learning.services.user_activity_service import UserActivityService




class ActivityProgressListCreateView(ListCreateAPIView):
    serializer_class = ActivityProgressSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = ActivityProgress.objects.filter(activity__user=self.request.user)
        
        return queryset

    def get_serializer_context(self):
        context = super(ActivityProgressListCreateView, self).get_serializer_context()

        activity_service = UserActivityService(self.request.user)
        activity_progress_service = ActivityProgresService(activity_service.activity)
        
        context.update({
            'request': self.request,    
            'activity_service': activity_service,
            'activity_progress_service': activity_progress_service
        })

        return context
    
class LessonLikeCreateView(ListCreateAPIView):
    serializer_class = LessonLikeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = LessonLike.objects.filter(user=self.request.user)
        return queryset        

    def get_serializer_context(self):
        context = super(LessonLikeCreateView, self).get_serializer_context()
        context.update({'request': self.request})

        return context
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LessonLikeDeleteView(DestroyAPIView):
    serializer_class = LessonLikeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = LessonLike.objects.filter(user=self.request.user)
        return queryset        

    def get_serializer_context(self):
        context = super(LessonLikeDeleteView, self).get_serializer_context()
        context.update({'request': self.request})

        return context

class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Lesson.objects.all()
        
        return queryset

    def get_serializer_context(self):
        context = super(LessonDetailView, self).get_serializer_context()

        context.update({'request': self.request})

        return context
    

class UserActivityDetailView(RetrieveAPIView):
    serializer_class = UserActivitySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = UserActivity.objects.filter(user=self.request.user)
        
        return queryset

    def get_serializer_context(self):
        context = super(UserActivityDetailView, self).get_serializer_context()
        context.update({'request': self.request})

        return context
    

class UserActivityListCreateView(ListCreateAPIView):
    serializer_class = UserActivitySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        queryset = UserActivity.objects.filter(user=self.request.user)
        
        return queryset

    def get_serializer_context(self):
        context = super(UserActivityListCreateView, self).get_serializer_context()

        activity_service = UserActivityService(self.request.user)


        context.update({
            'request': self.request,
            'activity_service': activity_service        
        })

        return context
    
        

class UserActivityLikeCreateView(ListCreateAPIView):
    serializer_class = UserActivityLikeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = UserActivityLike.objects.filter(user=self.request.user)
        return queryset        

    def get_serializer_context(self):
        context = super(UserActivityLikeCreateView, self).get_serializer_context()

        context.update({
            'request': self.request,
        })

        return context
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserActivityLikeDeleteView(DestroyAPIView):
    serializer_class = UserActivityLikeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = UserActivityLike.objects.filter(user=self.request.user)
        return queryset        

    def get_serializer_context(self):
        context = super(UserActivityLikeDeleteView, self).get_serializer_context()
        context.update({'request': self.request})

        return context
    
class UserActivityRatingCreateView(ListCreateAPIView):
    serializer_class = UserActivityRatingSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = UserActivityRating.objects.filter(user=self.request.user)
        return queryset        

    def get_serializer_context(self):
        context = super(UserActivityRatingCreateView, self).get_serializer_context()
        context.update({'request': self.request})

        return context
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)