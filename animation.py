import pygame


class Animation:
    def __init__(self, sheet, grid, size=None) -> None:
        """
        Initializes the Animation class to extract frames from a sprite sheet.

        :param sheet: Path to the sprite sheet image.
        :param grid: Tuple (columns, rows) representing the grid structure of the sprite sheet.
        :param size: Optional size of each sprite frame. If not provided, it is inferred from the sheet's size.
        """
        self.sheet = pygame.image.load(str(sheet)).convert_alpha()

        # If no specific size is given, calculate it based on the grid size
        if size is None:
            self.columns, self.rows = grid
            self.width = self.sheet.get_width() // self.columns
            self.height = self.sheet.get_height() // self.rows
        else:
            self.width, self.height = size
            self.columns, self.rows = grid

        self.frames = []
        self.extract_frames()

    def extract_frames(self):
        """
        Extracts frames from the sprite sheet based on the grid structure and stores them in self.frames.
        """
        for row in range(self.rows):
            frame_row = []
            for column in range(self.columns):
                frame = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                frame.blit(
                    self.sheet,
                    (0, 0),
                    (column * self.width, row * self.height, self.width, self.height),
                )
                frame.set_colorkey((0, 0, 0))  # Assuming black (0,0,0) is transparent
                frame = pygame.transform.scale_by(
                    frame, 2
                )  # Scaling the frame for better display
                frame_row.append(frame)
            self.frames.append(frame_row)
