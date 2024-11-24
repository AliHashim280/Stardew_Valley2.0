import pygame
import sys
import json

from settings import Settings
from player import Player
from tile_system import Tile_Map
from addresses import Tile_dir


class StardewValley2:
    """
    The main game class for Stardew Valley 2.0.
    Initializes the game, handles the game loop, and updates game elements.
    """

    def __init__(self) -> None:
        """
        Initialize the game settings, window, and player.
        """
        self.settings = Settings()  # Load game settings
        self.tile_directory = Tile_dir(self)  # Tile directory setup

        # Load the tile map from the directory
        self.load_tile_map()

        # Initialize Pygame
        pygame.init()

        # Screen setup
        self.setup_screen()

        # Background and player setup
        self.setup_background()
        self.setup_player()

        # Game clock
        self.clock = pygame.time.Clock()

    def load_tile_map(self):
        """
        Loads the tile map data from the JSON file.
        """
        with open(self.tile_directory.tile_map) as tile_map_file:
            data = json.load(tile_map_file)
            self.tile_map = data["tilemap"]

    def setup_screen(self):
        """
        Set up the Pygame screen and window.
        """
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(self.settings.game_name)

    def setup_background(self):
        """
        Set up the background (tile map) for the game.
        """
        self.BG = Tile_Map(self)
        self.tile_BG = self.BG.create_tile_screen(self.tile_map)

    def setup_player(self):
        """
        Initialize the player and set initial values.
        """
        self.player = Player(self)

    def update_tiles(self):
        """
        Update the game tiles.
        (Currently a placeholder method to be implemented later)
        """
        pass

    def update_player(self):
        """
        Update the player's state and draw them on the screen.
        """
        self.player.check_idle()
        self.player.select_frame_row()
        self.player.select_frame()
        self.player.update_player_pos()
        self.player.draw_frame(self)

    def handle_events(self):
        """
        Handle all game-related events (key presses, window close, etc.).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.player.handle_down_events(event)
            if event.type == pygame.KEYUP:
                self.player.handle_up_events(event)

    def run_game(self):
        """
        Run the main game loop.
        """
        while True:
            # Handle events (e.g., key presses, window events)
            self.handle_events()

            # Draw the background
            self.BG.draw_tile_screen(self)

            # Update player
            self.update_player()

            # Refresh the display
            pygame.display.flip()

            # Control the frame rate
            self.clock.tick(self.settings.fps)


# --- Entry Point ---
if __name__ == "__main__":
    game = StardewValley2()
    game.run_game()
