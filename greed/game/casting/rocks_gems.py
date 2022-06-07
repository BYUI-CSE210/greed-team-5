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

    def get_message(self):
        """Gets the artifact's message.

        Returns:
            string: The message.
        """
        return self._message

    def set_message(self, message):
        """Updates the message to the given one.

        Args:
            message (string): The given message.
        """
        self._message = message
