import numpy as np

from typing import TypeVar, List
from datetime import date


from apps.learning.models import UserActivity
from apps.learning.services.lesson_service import LessonService

from apps.authentication.tasks import create_timeline_item


T = TypeVar('T', bound=UserActivity)

class UserActivityService():
    """
    Service for UserActivity model
    """

    def __init__(self, user):
        self.user = user
        self.today = date.today()
        self.lesson_service = LessonService(user)

        if not self.check_if_activity_exists():
            self.activity = self.create_activity()
        else:
            self.activity = self.get_activity()


    def check_if_activity_exists(self) -> bool:
        """
        Check if the user has an activity for today

        Returns:
            bool: True if the user has an activity for today, False otherwise
        """
        return UserActivity.objects.filter(user=self.user, created_at__date=self.today).exists()
    
    def create_activity(self) -> T:
        """
        Create a new activity for the user

        Returns:
            T: UserActivity
        """

        lessons = self.lesson_service.set_activity_lessons()[::-1]

        print('lessons', lessons)


        activity = UserActivity.objects.create(
            title=f'My daily - {self.today.strftime("%A")}',
            user=self.user,
        )

        activity.lessons.add(*lessons)

        return activity
    
    def set_activity(self, slug: str) -> T or None:
        """
        Set the user's activity

        Args:
            slug (str): The slug of the activity

        Returns:
            T: UserActivity
        """
        try:
            activity = UserActivity.objects.get(slug=slug)
        except:
            return None

        self.activity = activity

        return activity
    
    def get_activity(self) -> T:
        """
        Get the user's activity for today

        Returns:
            T: UserActivity
        """
        return UserActivity.objects.get(user=self.user, created_at__date=self.today, user_activity_type='0')
    
    def get_last_activity(self) -> T or None:
        """
        Get the user's last activity

        Returns:
            T or None: UserActivity or None
        """
        try:
            return UserActivity.objects.filter(user=self.user).order_by('-created_at').first()
        except:
            return None
    
    def check_if_activity_completed(self) -> bool:
        """
        Check if the user has completed the activity for today

        Returns:
            bool: True if the user has completed the activity for today, False otherwise
        """
        if self.activity.progress.count() != self.activity.lessons.count():
            return False
        

        create_timeline_item.delay(
            user_id=self.user.id,
            action='0' if self.activity.user_activity_type == '0' else '2',
            item_id=self.activity.id,
        )

        return True
    
    def create_custom_activity(self, ref=T) -> T:
        """
        Create a custom activity for the user

        Args:
            title (str): The title of the activity
            lessons (List[int]): A list of lesson ids

        Returns:
            T: UserActivity
        """

        
        lessons = ref.lessons.all().reverse()

        activity = UserActivity.objects.create(
            title=f'Practice: {ref.title}',
            user=self.user,
            user_activity_type='1',
            parent=ref,
        )

        # add reversed lessons
        activity.lessons.add(*lessons)

        return activity
    
    # def process_new_user_score(self) -> int:
    #     """
    #     Process the user's score after completing an activity
    #     """
        
    #     WHEIGTHS = {
    #         'quiz_level_advanced': 5,
    #         'quiz_level_intermediate': 3,
    #         'quiz_level_beginner': 2,

    #         'lesson_level_advanced': 5,
    #         'lesson_level_intermediate': 3,
    #         'lesson_level_beginner': 2,

    #         'unknown_words': 3,
    #         'incorrect_answers': 1,

    #     }


    #     partial_scores = {
    #         'quiz_difficulty': 0,
    #         'lesson_difficulty': 0,
    #         'unknown_words': 0,
    #         'correct_answers': 0,
    #     }
