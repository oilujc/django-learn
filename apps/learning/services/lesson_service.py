from typing import TypeVar, List, Tuple
from random import choices, random

from functools import reduce
import operator

from django.db.models import Q

from apps.authentication.models import Interest
from apps.learning.models import Lesson

from apps.authentication.services.user_score_service import UserScoreService


L = TypeVar('L', bound=Lesson)
I = TypeVar('I', bound=Interest)


class LessonService():
    def __init__(self, user):
        self.user = user
        self.user_score_service = UserScoreService(user)

    def get_lesson(self, lesson_type: str, exclude: List[L] = [], epsilon: float = 0.1) -> L:
        """
        Get a lesson for the user

        Returns:
                L: Lesson
        """

        # Get user level
        min_level, max_level = self.get_user_level(epsilon)

        # Get lessons based on user interests and score
        qs = Q(
            lesson_type=lesson_type,
            level__lte=max_level,
            level__gte=min_level,
        )

        lessons = Lesson.objects.filter(qs)

        # Exclude lessons already seen
        if len(exclude) > 0:
            lessons = lessons.exclude(id__in=[l.id for l in exclude])

        # Get a random lesson
        return lessons.order_by('?').first()

    def get_user_level(self, epsilon=0.1) -> Tuple[int]:
        """
        Get the user's level interval [0, 5] - 0 Beginner, 5 Advanced 

        Args:
                epsilon (float, optional): Randomize level selection. Defaults to 0.1.

        Returns:
                List[int]: Level interval
        """

        user_level = self.user_score_service.get_score_level()

        # Randomize level selection
        if (random() < epsilon):
            # Get up to 2 levels above
            if user_level < 5:
                return (user_level + 1, user_level + 2)
            
            return (user_level - 1, user_level)


        if user_level > 5:
            return (4, 5)

        return (user_level, user_level + 1)

    def get_user_interests(self, epsilon=0.1) -> List[I]:
        """
        Get the user's interests

        Returns:
                List[I]: List of interests
        """

        if (random() < epsilon):
            # Randomize interests selection
            return choices(Interest.objects.all(), k=3)

        return self.user.interests.all()

    def get_next_lesson_type(self, last_lesson = None, epsilon=0.1) -> str:
        """
        Get the next lesson type for the user

        Returns:
                str: Lesson type
        """

        lesson_types = [key for key, value in Lesson.LESSON_TYPE_CHOICES]

        #TODO: remove this filter
        lesson_types = [lesson_type for lesson_type in lesson_types if lesson_type != '2' or lesson_type != '3']

        # Randomize lesson type selection
        if (random() < epsilon):
            return choices(lesson_types, k=1)[0]

        if not last_lesson:
            return choices(lesson_types, k=1)[0]

        return choices([lesson_type for lesson_type in lesson_types if lesson_type != last_lesson.lesson_type], k=1)[0]

    def set_activity_lessons(self, max=4) -> List[L]:
        """
        Get the lessons for the user's activity

        Args:
            max (int, optional): Max lessons for activity. Defaults to 4.

        Returns:
            List[L]: List of lessons
        """

        lessons = []
        last_lesson = None
        epsilon = 0.1

        while len(lessons) < max:

            lesson_type = self.get_next_lesson_type(last_lesson=last_lesson)
            lesson = self.get_lesson(lesson_type, exclude=[l for l in lessons if l is not None], epsilon=epsilon)

            print('lesson', lesson, lesson_type)
            if not lesson:
                # If no lesson is found, increase randomization
                epsilon += 0.01
                continue

            lessons.append(lesson)
            last_lesson = lesson



        # Sort by level
        lessons = sorted(lessons, key=lambda lesson: lesson.level)

        print('lessons', lessons)

        return lessons