

import numpy as np

from apps.learning.services.user_activity_service import UserActivityService


class ActivityWheightService(object):
    """Service to calculate the activity recommendations weight of a user."""

    def __init__(self, user):
        self.user = user
        self.user_activity_service = UserActivityService(user)

    def recommend_custom_activities(self, max=4) -> list:
        """Recommend custom activities to the user.

        Args:
            max (int, optional): Max number of activities to recommend. Defaults to 4.

        Returns:
            list: List of activities
        """
        pass

    def recommend_user_similar_activities(self, max=4) -> list:
        """Recommend activities similar to the user's activities.

        Args:
            max (int, optional): Max number of activities to recommend. Defaults to 4.

        Returns:
            list: List of activities
        """
        pass

    def recommend_user_interests_activities(self, max=4) -> list:
        """Recommend activities based on the user's interests.

        Args:
            max (int, optional): Max number of activities to recommend. Defaults to 4.

        Returns:
            list: List of activities
        """
        pass

    def recommend_user_level_activities(self, max=4) -> list:
        """Recommend activities based on the user's level.

        Args:
            max (int, optional): Max number of activities to recommend. Defaults to 4.

        Returns:
            list: List of activities
        """
        pass

    def recommend_user_score_activities(self, max=4) -> list:
        """Recommend activities based on the user's score.

        Args:
            max (int, optional): Max number of activities to recommend. Defaults to 4.

        Returns:
            list: List of activities
        """
        pass

    def recommend_user_likes_activities(self, max=4) -> list:
        """Recommend activities based on the user's likes.

        Args:
            max (int, optional): Max number of activities to recommend. Defaults to 4.

        Returns:
            list: List of activities
        """
        pass



