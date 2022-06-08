from game.casting.actor import Actor
from game.shared.point import Point


class Objects(Actor):
    """
    Are items (gems and rocks) if the robot touch a rock lose a point, if is gem win one point. 

    The responsibility of Objects is to keep the score of gain or lose points.

    Attributes:
        _score (int): tracking of the score.
    """

    def __init__(self):
        super().__init__()
        self._score = 0

    def get_score(self):
        """Gets the points.

        Returns:
            int: The points.
        """
        return self._score

    def set_score(self, points):
        """Updates the points gained or lose every the robot touch
        one object

        Args:
            points (int): The given points.
        """
        self._score = points
