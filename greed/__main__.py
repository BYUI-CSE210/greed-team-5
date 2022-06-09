import os
import random
from pyparsing import White

from raylib import DEFAULT

from game.casting.actor import Actor
from game.casting.rocks_gems import Objects
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed game"
WHITE = Color(255, 255, 255)
GEMS_ROCKS = 40


def main():

    # create the cast
    cast = Cast()

    # create the banners
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    banner1 = Actor()
    banner1.set_text("")
    banner1.set_font_size(FONT_SIZE)
    banner1.set_color(WHITE)
    banner1.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner1)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    #place the player to the bottom of the screen
    start_position_y = -15
    position = Point(x, y)
    position_robot = Point(x , start_position_y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    #robot.set_position(position)
    robot.set_position(position_robot)
    cast.add_actor("robots", robot)

    # create the gems and rocks

    dx = 0
    dy = int(CELL_SIZE / 3)
    direction = Point(dx, dy)

    for n in range(GEMS_ROCKS):

        if n < int(GEMS_ROCKS/2):
            text = "*"
            points = 1
        else:
            text = "O"
            points = -1

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)

        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact = Objects()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_score(points)
        artifact.set_velocity(direction)
        cast.add_actor("artifacts", artifact)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(
        CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
