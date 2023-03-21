"""Turtle Racing Game - Player Class

This module implements the Player class for the Turtle Racing Game.
The Player class represents a turtle player in the game, and provides
methods for moving the player's turtle forward, getting the x-coordinate
of the turtle, and getting the color of the turtle.
"""


import turtle as t



class Player:
    """A class representing a turtle player."""

    def __init__(self, x: int, y: int, color: str):
        """Initializes the Player object.

        Args:
            x (int): The initial x-coordinate of the player.
            y (int): The initial y-coordinate of the player.
            color (str): The color of the player's turtle.
        """
        # a turtle shaped player and make it visible when created
        self.turtle = t.Turtle(shape="turtle", visible=False)
        self.turtle.penup()
        self.turtle.goto(x=x, y=y)
        self.turtle.color(color)
        # show the turtle player once they are moved to the starting line
        self.turtle.showturtle()
    
    # Behaviors: move(), get_xcor(), get_color()
    def move_forward(self, distance):
        """Moves the player's turtle forward a given distance.

        Args:
            distance (int): The distance to move the turtle forward.
        """
        self.turtle.forward(distance)

    def get_xcor(self):
        """Returns the x-coordinate of the player's turtle.

        Returns:
            float: The x-coordinate of the turtle.
        """
        return self.turtle.xcor()

    def get_color(self):
        """Returns the color of the player's turtle.

        Returns:
            str: The color of the turtle.
        """
        return self.turtle.pencolor()

# test Player class
if __name__ == "__main__":
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    STARTING_X_POS = -SCREEN_WIDTH / 2 + 50
    FINISH_X_POS = SCREEN_WIDTH / 2 - 50

    screen = t.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    
    player = Player(0, 0, "blue")

    screen.exitonclick()
