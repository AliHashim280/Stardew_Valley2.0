from pathlib import Path


class Tile_dir:
    def __init__(self, game) -> None:
        """
        Initialize the Tile_dir class with paths for various resources like sprites
        and the tile map JSON.
        """
        self.Base_Dir = game.settings.BASE_DIR

        # Paths for different tile images
        self.simple_tiles = (
            self.Base_Dir / "sprites" / "sprites" / "tilesets" / "decor_8x8.png"
        )
        self.wooden_floor = (
            self.Base_Dir / "sprites" / "sprites" / "tilesets" / "floors" / "wooden.png"
        )
        self.grass = self.Base_Dir / "sprites" / "2" / "Texture" / "grass.png"

        # Path to the tile map JSON file
        self.tile_map = self.Base_Dir / "data" / "tile_map.json"
