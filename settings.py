import pygame
from pathlib import Path


class Settings:
    def __init__(self) -> None:
        """
        Initialize the game settings, including screen dimensions,
        player attributes, and file paths.
        """
        self.game_name = "Stardew Valley 2.0"  # Game title
        self.SCREEN_WIDTH = 800  # Screen width
        self.SCREEN_HEIGHT = 600  # Screen height
        self.BG = (50, 50, 50)  # Background color (RGB)
        self.TILE_SIZE = 32  # Size of each tile in pixels

        # Player settings
        self.player_speed_pixels = 2  # Player speed in pixels
        self.player_tile_speed = (
            1  # Player speed in tiles per second (1 tile = 32 pixels)
        )

        # Movement and animation settings
        self.movement_delay = 16  # Movement update delay in milliseconds
        self.animation_delay = 125  # Animation frame delay in milliseconds

        # Game's base directory for file paths
        self.BASE_DIR = Path(__file__).resolve().parent

        # Frames per second for the game loop
        self.fps = 60

        # Optional: Add more settings if needed (e.g., sound settings, difficulty, etc.)

    def get_screen_size(self):
        """
        Returns the screen size as a tuple (width, height).
        """
        return self.SCREEN_WIDTH, self.SCREEN_HEIGHT

    def get_background_color(self):
        """
        Returns the background color.
        """
        return self.BG

    def get_tile_size(self):
        """
        Returns the size of a tile in the game.
        """
        return self.TILE_SIZE

    def get_player_speed(self):
        """
        Returns the speed of the player in pixels.
        """
        return self.player_speed_pixels

    def get_player_tile_speed(self):
        """
        Returns the player's speed in tiles per second.
        """
        return self.player_tile_speed

    def get_movement_delay(self):
        """
        Returns the movement delay in milliseconds.
        """
        return self.movement_delay

    def get_animation_delay(self):
        """
        Returns the animation frame delay in milliseconds.
        """
        return self.animation_delay
