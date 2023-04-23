from typing import TypeVar, List
from random import choices, random

from apps.learning.models import ActivityProgress, UserActivity, Lesson

P = TypeVar('P', bound=ActivityProgress)
A = TypeVar('A', bound=UserActivity)
L = TypeVar('L', bound=Lesson)


class ActivityProgresService():
	def __init__(self, activity: A):
		self.activity = activity

	def create_progress(self, lesson: L) -> P:
		"""
		Create a new progress for the user        

		Returns:
				P: ActivityProgress
		"""

		# Get Activity progress
		activity_progress = self.activity.progress.all()

		# Get excluded lessons
		exclude = [p.lesson.id for p in activity_progress]

		# Get current lessons
		lessons = self.activity.lessons.exclude(
			id__in=[*exclude, lesson.id]
		)
		# Get the next lesson
		next_lesson = None

		if len(lessons) > 0:
			next_lesson = lessons.first()

		activity_progress = ActivityProgress.objects.create(
			activity=self.activity,
			lesson=lesson,
			next_lesson=next_lesson,
		)

		return activity_progress
	

	def check_if_progress_exists(self, lesson: L) -> bool:
		"""
		Check if the user has a progress for the lesson

		Returns:
				bool: True if the user has a progress for the lesson, False otherwise
		"""
		return ActivityProgress.objects.filter(
			activity=self.activity,
			lesson=lesson,
		).exists()
	
	def get_next_lesson(self, num: int = 1) -> List[L] or None:
		"""_summary_

		Args:
			num (int, optional): Number of elements to be returned. Defaults to 1.
		
		Returns:
			L: _description_
		"""

		activity_progress = self.activity.progress.all()
		lessons = self.activity.lessons.all()

		if len(activity_progress) == 0:
			return lessons[:num] if num != 1 and len(lessons) >= num else [lessons.first()]

		lessons = self.activity.lessons.exclude(
			id__in=[p.lesson.id for p in activity_progress]
		)

		if len(lessons) == 0:
			return None
		
		if num != 1 and len(lessons) >= num:
			return lessons[:num]

		return [lessons.first()]


	def validate_lesson(self, lesson: L) -> bool:
		"""
		Validate if the lesson is valid for the user

		Returns:
						bool: True if the lesson is valid, False otherwise
		"""
		# Check if the lesson is in the activity
		if not self.activity.lessons.filter(id=lesson.id).exists():
			return False, 'not_in_activity'

		# Check if the lesson is in the progress
		if self.check_if_progress_exists(lesson):
			return False, 'already_in_progress'

		# Check if the lesson is the next lesson
		last_progress = self.activity.progress.last()

		if last_progress and last_progress.next_lesson != lesson:
			return False, 'not_next_lesson'

		return True, None
