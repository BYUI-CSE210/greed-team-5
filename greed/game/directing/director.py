"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/inheritance/materials/greed-specification.html
"""
from game.shared.point import Point


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._total_score = 0
        self._banner1 = 10
        self._banner1_x = 0
        self._banner1_y = 0

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_actor("banners")
        robot = cast.get_actor("robots")
        artifacts = cast.get_actors("artifacts")
        banner1 = cast.get_actor("banners", 1)

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        self._banner1 -= 1
        if self._banner1 < 1:
            banner1.set_text("")
        else: banner1.set_position(Point(self._banner1_x, self._banner1_y + (self._banner1-14)))

        for artifact in artifacts:

            artifact.move_next(max_x, max_y)

            if robot.get_position().equals(artifact.get_position()):
                self._total_score += artifact.get_score()

                banner.set_text(f"score: {self._total_score}")

                current_position = artifact.get_position()
                new_position = Point(current_position.get_x(), 0)
                artifact.set_position(new_position)

                self._banner_display(cast, artifact, current_position)



    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
    
    def _banner_display(self, cast, artifact, position):
        """Creates and displays banners for the game.
        
        Args:
            cast (Cast): The cats of actors
        """
        banner = cast.get_actor("banners", 1)
        self._banner1_x = Point.get_x(position)
        self._banner1_y = Point.get_y(position) - 15

        if artifact.get_score() > 0:
            banner.set_text("+1")
        else: banner.set_text("-1")

        banner.set_position(Point(self._banner1_x, self._banner1_y))
        self._banner1 = 10
