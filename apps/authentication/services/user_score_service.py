import numpy as np

class UserScoreService():
    def __init__(self, user):
        self.user = user

    def get_score_level(self) -> int:
        """
            Get the user's level based on the user's score
        """

        score = self.get_user_score()

        if score < 100:
            return 0
        elif score < 200:
            return 1
        elif score < 300:
            return 2
        elif score < 400:
            return 3
        elif score < 500:
            return 4

        return 5
    
    def get_user_score(self) -> int:
        """
            Get the user's score
        """
        return self.user.profile.score
    
