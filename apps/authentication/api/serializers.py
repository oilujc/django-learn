
from rest_framework import serializers
from apps.authentication.models import Interest, TimelineItem

from apps.learning.api.serializers import UserActivitySerializer, LessonSerializer

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'interest')


class UserInterestSerializer(serializers.Serializer):
    interests_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        write_only=True
    )

    def save(self):

        user = self.context['request'].user
        interests = self.validated_data.get('interests_ids', [])

        user.interests.clear()
        user.interests.add(*interests)

        user.save()

    def validate(self, attrs):
        interests = attrs.get('interests_ids', [])

        if not interests:
            raise serializers.ValidationError('Please select at least one interest.')
        
        if len(interests) > 6:
            raise serializers.ValidationError('Please select only 6 interests.')

        return attrs


class TimelineItemSerializer(serializers.ModelSerializer):
    
    item = serializers.SerializerMethodField()
    action = serializers.SerializerMethodField()

    class Meta:
        model = TimelineItem
        fields = ('id', 'action', 'item', 'created_at')

    def get_action(self, obj):
        return dict(TimelineItem.ACTIONS_CHOICES)[obj.action]
    
    def get_item(self, obj):
        action = dict(TimelineItem.ACTIONS_CHOICES)[obj.action]
        
        if action == 'daily_activity_completed' or action == 'custom_activity_completed':

            return UserActivitySerializer(obj.timeline.first().activity, context={
                'request': self.context['request']
            }).data
        
        if action == 'single_lesson_completed':
            return LessonSerializer(obj.lesson_timeline.first().lesson, context={
                'request': self.context['request']
            }).data
        
        return None