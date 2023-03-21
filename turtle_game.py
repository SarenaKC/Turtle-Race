"""Turtle Racing Game - Game class

This module implements the Game class for the Turtle Racing Game.
"""


import turtle as t
import random

from turtle_player import Player


class Game:
    """The Game class sets up the game window and contains the logic of the game."""

    def __init__(self, colors=None):
        """Initialize the Game class.

        Args:
            colors (list of str, optional): A list of colors for the turtle players.
            Defaults to None.
        """
        # Set up the screen
        self.screen = t.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Turtle Racing Game")

        # A list to store players
        self.players = []
        # A list of pre-selected colors
        if colors is None:
            self.colors = ["lime green", "dark orange", "dark violet", "deep sky blue"]
        else:
            self.colors = colors
        # Starting and Ending x-coordinates of the Player
        self.starting_x_pos = -self.screen.window_width() / 2 + 50
        self.finish_x_pos = self.screen.window_width() / 2 - 50

        # Related to game control
        self.is_race_on = False
        self.user_picked_winner = ""

    # TODO: Keep impvoring the setup_player to make it more robust?
    def setup_player(self):
        """Initialize the turtle players.

        This method set up each player's starting positions based on the number of players
        and the available height of the screen. Each player is assigned a color
        from the list of colors provided during initialization of the Game class.
        The players are then created using the Player class and added to the list of players.
        """
        num_of_players = len(self.colors)
        # padding: space between players and the edges of the window
        padding = 50
        available_height = self.screen.window_height() - 2 * padding
        space_for_player = available_height / num_of_players
        # A list to store starting y-coordinates for each player
        y_coordinates = (
            [available_height / 2 - padding - i * space_for_player
             for i in range(num_of_players)]
        )

        # Create a player with a specific color and add to the players list
        for i, color in enumerate(self.colors):
            player = Player(x=self.starting_x_pos, y=y_coordinates[i], color=color)
            self.players.append(player)

    def ask_user_for_winner(self):
        """Ask user the color of the winning player."""
        self.user_picked_winner = self.screen.textinput(title="Who's the winner?",
                                           prompt="Which player will win the race?")
        self.user_picked_winner = self.user_picked_winner.lower()

    def start_race(self):
        """Start the race."""
        self.is_race_on = True
        while self.is_race_on:
            for player in self.players:
                player.move_forward(random.randint(0, 20))
                if player.get_xcor() > self.finish_x_pos:
                    self.is_race_on = False
                    winner = player.get_color()
                    if winner == self.user_picked_winner:
                        print(f"You won! The winner's color is {winner}!")
                    else:
                        print("Sorry, your player didn't win...\n"
                             f"The winner's color is {winner}!")
  
    def run_game(self):
        """Run the turtle racing game."""
        self.ask_user_for_winner()
        self.setup_player()
        self.start_race()
        self.screen.exitonclick()

if __name__ == "__main__":
    game = Game()
    game.run_game()
