import pygame
from animation import Animation
from math import sqrt


class Player:
    def __init__(self, game) -> None:
        """
        Initialize the Player class with settings, animations, and movement properties.
        """
        # --- Animation Settings ---
        self.player_sheet_path = (
            game.settings.BASE_DIR / "sprites" / "sprites" / "characters" / "player.png"
        )
        self.animation = Animation(
            self.player_sheet_path,
            (6, 9),  # Grid size of spritesheet (columns, rows)
            (48, 48),  # Dimensions of each frame
        )

        # --- Position and Movement Settings ---
        self.x = self.y = 0  # Initial player position
        self.speed = game.settings.player_speed_pixels  # Movement speed in pixels
        self.frame_delay = game.settings.animation_delay  # Animation frame delay
        self.current_frame = 0  # Current frame in animation
        self.last_updated = (
            pygame.time.get_ticks()
        )  # Last time animation frame was updated

        # --- Direction and State Settings ---
        self.direction_map = {  # Map directions to rows, frames, and flip states
            "up": (2, 5, False),  # Row for idle, row for walking, flip horizontally
            "down": (0, 3, False),
            "left": (1, 4, True),
            "right": (1, 4, False),
        }
        self.direction_key = "down"  # Default direction
        self.horizontal_flip = False  # Whether to flip sprite horizontally
        self.idle = True  # Is the player idle?

        # --- Animation and Key States ---
        self.current_row = self.direction_map[self.direction_key][
            0
        ]  # Current animation row
        self.up = self.down = self.right = self.left = False  # Movement keys state
        self.game = game  # Reference to the game object

    # --- Event Handling ---
    def handle_down_events(self, event):
        """
        Handle key press events for movement.
        """
        if event.key == pygame.K_w:
            self.up, self.direction_key = True, "up"
            self.down = False
        elif event.key == pygame.K_s:
            self.down, self.direction_key = True, "down"
            self.up = False
        if event.key == pygame.K_a:
            self.left, self.direction_key = True, "left"
            self.right = False
        elif event.key == pygame.K_d:
            self.right, self.direction_key = True, "right"
            self.left = False

    def handle_up_events(self, event):
        """
        Handle key release events for movement.
        """
        if event.key == pygame.K_w:
            self.up = False
        elif event.key == pygame.K_s:
            self.down = False
        elif event.key == pygame.K_a:
            self.left = False
        elif event.key == pygame.K_d:
            self.right = False

    # --- State Updates ---
    def check_idle(self):
        """
        Check if the player is idle based on key states.
        """
        self.idle = not (self.up or self.down or self.left or self.right)

    def select_frame_row(self):
        """
        Select the appropriate animation row based on direction and idle state.
        """
        animation_data = self.direction_map[self.direction_key]
        self.current_row = animation_data[0] if self.idle else animation_data[1]
        self.horizontal_flip = animation_data[2]

    def update_player_pos(self):
        """
        Update the player's position based on movement direction.
        """
        dx = dy = 0

        # Movement logic
        dy -= self.speed if self.up else 0
        dy += self.speed if self.down else 0
        dx += self.speed if self.right else 0
        dx -= self.speed if self.left else 0

        # Diagonal movement adjustment (normalize movement)
        if dx and dy:
            speed_adjust = 1 / sqrt(2)
            dx *= speed_adjust
            dy *= speed_adjust

        self.x += dx
        self.y += dy

    # --- Animation Updates ---
    def select_frame(self):
        """
        Select the current animation frame based on elapsed time.
        """
        now = pygame.time.get_ticks()
        if now - self.last_updated > self.frame_delay:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(
                self.animation.frames[self.current_row]
            )

    def get_new_tile(self):
        """
        Placeholder for future tile updates based on player position (to be implemented).
        """
        pass

    def draw_frame(self, game):
        """
        Draw the current animation frame on the game screen.
        """
        frame = self.animation.frames[self.current_row][self.current_frame]
        if self.horizontal_flip:
            frame = pygame.transform.flip(frame, True, False)

        game.screen.blit(frame, (self.x, self.y))
