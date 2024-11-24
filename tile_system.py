import pygame
from addresses import Tile_dir
import json


class TileSet:
    def __init__(self, sheet, grid, size=None) -> None:
        """
        Initializes the TileSet class to extract tiles from a sprite sheet.

        :param sheet: Path to the spritesheet image.
        :param grid: Tuple (columns, rows) that defines the grid size.
        :param size: Optional tile size. If not provided, it will be automatically calculated.
        """
        self.sheet = pygame.image.load(str(sheet)).convert_alpha()

        # If size is not provided, calculate it based on the sprite sheet size and grid.
        if size is None:
            self.columns, self.rows = grid
            self.width = self.sheet.get_width() / self.columns
            self.height = self.sheet.get_height() / self.rows
        else:
            self.width, self.height = size
            self.columns, self.rows = grid

        self.tiles = []
        self.extract_tiles()

    def extract_tiles(self):
        """
        Extracts all tiles from the spritesheet and stores them in the self.tiles list.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                # Create a new surface to hold the tile (width x height)
                tile = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

                # Blit the specific portion of the sheet to the tile surface
                tile.blit(
                    self.sheet,
                    (0, 0),  # Blit to the top-left corner of the tile surface
                    (column * self.width, row * self.height, self.width, self.height),
                )

                tile.set_colorkey(
                    (0, 0, 0)
                )  # Assuming black (0,0,0) is the transparent color.
                self.tiles.append(tile)  # Add the extracted tile to the list

    def get_tile(self, index):
        """
        Get a specific tile by index.

        :param index: Index of the tile in the list.
        :return: The tile surface at the specified index.
        """
        return self.tiles[index] if 0 <= index < len(self.tiles) else None


class Tile_Map:
    def __init__(self, game) -> None:
        """
        Initializes the Tile_Map class that manages tile-related operations.
        """
        self.tiles = Tile_dir(game)

        # Initialize tile set using the grass texture
        self.tile_set = TileSet(self.tiles.grass, (7, 7))

        self.game = game
        self.size = game.settings.TILE_SIZE

        # Calculate the number of tiles that fit on the screen
        self.tile_x = game.settings.SCREEN_WIDTH / self.size
        self.tile_y = game.settings.SCREEN_HEIGHT / self.size

    def create_tile_screen(self, tile_map):
        """
        Creates a surface for the entire tile map to be rendered on the screen.

        :param tile_map: The 2D list representing the tile map.
        :return: The surface containing the rendered tile map.
        """
        tile_screen = pygame.Surface(
            (self.game.settings.SCREEN_WIDTH, self.game.settings.SCREEN_HEIGHT)
        )

        # Iterate through the tile map and render each tile at the appropriate position
        for y, row in enumerate(tile_map):
            for x, tile in enumerate(row):
                tile_screen.blit(
                    self.tile_set.get_tile(tile), (x * self.size, y * self.size)
                )

        return tile_screen

    def draw_tile_screen(self, game):
        """
        Draws the tile map onto the game screen.

        :param game: The game instance to render the tile map.
        """
        game.screen.blit(game.tile_BG, (0, 0))
