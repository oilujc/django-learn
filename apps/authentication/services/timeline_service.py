from typing import TypeVar, Any

from apps.authentication.models import TimelineItem
from apps.learning.models import ActivityTimeline, LessonTimeline

T = TypeVar('T', bound=TimelineItem)
A = TypeVar('A', bound=ActivityTimeline)
L = TypeVar('L', bound=LessonTimeline)

class TimelineService():
    def __init__(self, user):
        self.user = user
        self.msg = None

    def get_timeline(self, id: int) -> T or None:
        """
        Get a timeline item

        Args:
            id (int): The id of the timeline item

        Returns:
            T: TimelineItem
        """
        try:
            return TimelineItem.objects.get(id=id)
        except TimelineItem.DoesNotExist:
            return None
        
    def get_timeline_items(self) -> list:
        """
        Get all timeline items for the user

        Returns:
            list: TimelineItem
        """
        return TimelineItem.objects.filter(user=self.user)
    
    def create_timeline_item(self, action: str, item_id: int) -> T:
        """
        Create a new timeline item

        Args:
            action (str): The action that was performed
            item (Any): The item that was affected

        Returns:
            T: TimelineItem
        """

        if (action == '0' or action == '2') and self.check_if_activity_timeline_exists(item_id):
            self.msg = 'Activity already completed'

            return None
            
        elif action == '1' and self.check_if_lesson_timeline_exists(item_id):
            self.msg = 'Lesson already completed'

            return None


        timeline_item = TimelineItem.objects.create(
            user=self.user,
            action=action,
        )

        if action == '0' or action == '2':
            self.create_activity_timeline(timeline_item, item_id)
            
        elif action == '1':
            self.create_lesson_timeline(timeline_item, item_id)

        return timeline_item
        

    def check_if_activity_timeline_exists(self, item_id: int) -> bool:
        """
        Check if the activity timeline exists

        Args:
            item (Any): The item that was affected

        Returns:
            bool: True if the activity timeline exists, False otherwise
        """
        return ActivityTimeline.objects.filter(
            timeline__user=self.user,
            activity=item_id
        ).exists()


    def create_activity_timeline(self, timeline_item: T, item_id: int) -> A:
        """
        Create a new activity timeline item

        Args:
            timeline_item (T): The activity item that was completed
            item (Any): The item that was affected

        Returns:
            A: ActivityTimeline
        """

        return ActivityTimeline.objects.create(
            timeline=timeline_item,
            activity_id=item_id
        )

    def check_if_lesson_timeline_exists(self, item_id: int) -> bool:
        """
        Check if the lesson timeline exists

        Args:
            item (Any): The item that was affected

        Returns:
            bool: True if the lesson timeline exists, False otherwise
        """
        return LessonTimeline.objects.filter(
            timeline__user=self.user,
            lesson=item_id
        ).exists()


    def create_lesson_timeline(self, timeline_item: T, item_id: int) -> L:
        """
        Create a new lesson timeline item

        Args:
            timeline_item (T): The lesson item that was completed
            item (Any): The item that was affected

        Returns:
            L: LessonTimeline
        """

        return LessonTimeline.objects.create(
            timeline=timeline_item,
            lesson_id=item_id
        )