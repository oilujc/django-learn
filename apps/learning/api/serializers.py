from rest_framework import serializers
from apps.learning.models import Lesson, ActivityProgress, LessonLike, UserActivity, UserActivityLike, UserActivityRating


class LessonListSerializer(serializers.ModelSerializer):

    lesson_type = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'slug', 'lesson_type', 'level' )

    def get_lesson_type(self, obj):
        return dict(obj.LESSON_TYPE_CHOICES)[obj.lesson_type]
    
class ActivityProgressList(serializers.ModelSerializer):

    class Meta:
        model = ActivityProgress
        fields = ('id', 'lesson')


class UserActivitySerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()
    progress_count = serializers.SerializerMethodField()
    is_rating = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    user_progress = serializers.SerializerMethodField()
    user_activity_type = serializers.SerializerMethodField()
    child = serializers.SerializerMethodField()

    ref = serializers.CharField(source='slug', write_only=True)

    class Meta:
        model = UserActivity
        fields = (
            'id', 
            'title', 
            'slug', 
            'lessons', 
            'lesson_count', 
            'progress_count', 
            'user_progress', 
            'is_rating', 
            'is_liked', 
            'ref', 
            'child',
            'user_activity_type',
            'created_at', 
            'updated_at'
        )
        read_only_fields = ('id', 
            'title', 
            'slug', 
            'lessons', 
            'lesson_count', 
            'progress_count', 
            'user_progress', 
            'is_rating', 
            'is_liked', 
            'child',
            'user_activity_type',
            'created_at', 
            'updated_at'
        )


    def validate(self, attrs):

        print(attrs)
        ref = attrs['slug']

        try:
            attrs['slug'] = UserActivity.objects.get(slug=ref)

        except UserActivity.DoesNotExist:
            raise serializers.ValidationError("Activity does not exist")


        return super().validate(attrs)
        

    def create(self, validated_data):

        activity_service = self.context['activity_service']
        activity = activity_service.create_custom_activity(validated_data['slug'])


        return activity


    def get_child(self, obj):
        return [child.slug for child in obj.children.all()]

    def get_user_activity_type(self, obj):
        return dict(obj.USER_ACTIVITY_TYPE_CHOICES)[obj.user_activity_type]

    def get_lesson_count(self, obj):
        return obj.lessons.count()
    
    def get_progress_count(self, obj):
        return obj.progress.count()
    
    def get_is_rating(self, obj):
        return obj.ratings.filter(user=self.context['request'].user).exists()
    
    def get_is_liked(self, obj):
        return obj.followers.filter(user=self.context['request'].user).exists()
    
    def get_lessons(self, obj):
        return LessonListSerializer(obj.lessons.all(), many=True).data

    def get_user_progress(self, obj):
        return ActivityProgressList(obj.progress.all(), many=True).data

class LessonLikeSerializer(serializers.ModelSerializer):

    class Meta:

        model= LessonLike
        fields= ('id', 'lesson', 'created_at', 'updated_at')

    def validate(self, attrs):

        user = self.context['request'].user
        lesson = attrs['lesson']

        if lesson.lesson_likes.filter(user=user).exists():
            raise serializers.ValidationError("You already liked this lesson")

        return super().validate(attrs)

class LessonSerializer(serializers.ModelSerializer):

    content = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    lesson_type = serializers.SerializerMethodField()


    class Meta:

        model = Lesson

        fields = ('id', 'title', 'slug', 'is_liked', 'short_description', 'content', 'created_at', 'updated_at', 'lesson_type', 'image', 'level', 'interests')
        read_only_fields = ('slug', 'is_liked', 'created_at', 'updated_at', 'lesson_type', 'image', 'level', 'interests')

    def get_content(self, obj):
        return obj.content.html
    
    def get_is_liked(self, obj):
        user = self.context['request'].user

        try:
            is_like = obj.lesson_likes.get(user=user)
            is_like = LessonLikeSerializer(is_like).data

        except LessonLike.DoesNotExist:
            is_like = None

        return is_like

    def get_lesson_type(self, obj):
        return dict(obj.LESSON_TYPE_CHOICES)[obj.lesson_type]

class ActivityProgressSerializer(serializers.ModelSerializer):

    next_lesson = serializers.SerializerMethodField()
    ref = serializers.CharField(source='activity.slug', write_only=True)

    class Meta:

        model = ActivityProgress

        fields = ('id', 'activity', 'lesson', 'next_lesson', 'ref', 'created_at', 'updated_at')
        read_only_fields = ('id', 'activity', 'next_lesson', 'created_at', 'updated_at')

    def validate(self, attrs):

        ref = attrs['activity']['slug']
        lesson = attrs['lesson']

   
        try:
            attrs['activity'] = UserActivity.objects.get(slug=ref)

        except UserActivity.DoesNotExist:
            raise serializers.ValidationError("Activity does not exist")
        

        activity_progress_service = self.context['activity_progress_service']
        activity_progress_service.activity = attrs['activity']

        is_valid, msg = activity_progress_service.validate_lesson(lesson)

        if not is_valid:
            raise serializers.ValidationError(f'Lesson is not valid code: {msg}')


        return super().validate(attrs)

    def create(self, validated_data):

        print('validated_data', validated_data)

        lesson = validated_data['lesson']

        activity_progress_service = self.context['activity_progress_service']
        activity_service = self.context['activity_service']

        activity_service.activity = validated_data['activity']

        progress = activity_progress_service.create_progress(lesson)
        activity_service.check_if_activity_completed()

        return progress
    
    
    def get_next_lesson(self, obj):
        return LessonSerializer(obj.next_lesson, context=self.context).data if obj.next_lesson else None


class UserActivityLikeSerializer(serializers.ModelSerializer):
    
        class Meta:
    
            model = UserActivityLike
            fields = ('id', 'activity', 'created_at', 'updated_at')
    
        def validate(self, attrs):
    
            user = self.context['request'].user
            activity = attrs['activity']

            if activity.followers.filter(user=user).exists():
                raise serializers.ValidationError("You already liked this activity")
            

            return super().validate(attrs)


class UserActivityRatingSerializer(serializers.ModelSerializer):
    
        class Meta:
    
            model = UserActivityRating
            fields = ('id', 'activity', 'rating', 'created_at', 'updated_at')
    
        def validate(self, attrs):
    
            user = self.context['request'].user
            activity = attrs['activity']
    
            if activity.ratings.filter(user=user).exists():
                raise serializers.ValidationError("You already rated this activity")
    
            return super().validate(attrs)

        def validate_rating(self, value):
            if value < 1 or value > 5:
                raise serializers.ValidationError("Rating must be between 1 and 5")
            return value
