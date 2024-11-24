# Old Player

import pygame
from animation import Animation
import sys


class Player:
    def __init__(self, game) -> None:
        self.player_sheet_path = (
            game.settings.BASE_DIR / "sprites" / "sprites" / "characters" / "player.png"
        )

        self.animation = Animation(
            self.player_sheet_path,
            (6, 9),
            (48, 48),
        )
        self.x, self.y = 0, 0
        self.speed = game.settings.player_speed
        self.frame_delay = game.settings.animation_delay
        self.current_frame = 0
        self.last_updated = pygame.time.get_ticks()

        self.horizontal_flip = False
        self.directions = {"down": 0, "right": 1, "up": 2, "left": 1}
        self.direction = self.directions["down"]
        self.current_row = self.direction
        self.up = self.down = self.right = self.left = False
        self.game = game

    def handle_down_events(self, event):
        if event.key == pygame.K_w:
            self.up, self.direction = True, self.directions["up"]
        elif event.key == pygame.K_s:
            self.down, self.direction = True, self.directions["down"]
        elif event.key == pygame.K_a:
            self.left, self.direction, self.current_row = (
                True,
                self.directions["left"],
                4,
            )
        elif event.key == pygame.K_d:
            self.right, self.direction, self.current_row = (
                True,
                self.directions["right"],
                4,
            )

    def handle_up_events(self, event):
        if event.key == pygame.K_w:
            self.up, self.current_row = False, self.directions["up"]
        elif event.key == pygame.K_s:
            self.down, self.current_row = False, self.directions["down"]
        elif event.key == pygame.K_a:
            self.left, self.current_row = False, self.directions["left"]
        elif event.key == pygame.K_d:
            self.right, self.current_row = False, self.directions["right"]

    def validate_keys(self):
        # Prevent both horizontal or vertical movement in opposite directions
        if (self.left and self.right) or (self.up and self.down):
            self.horizontal_flip = self.direction == self.directions["left"]
            self.direction = (
                self.directions["right"]
                if self.direction == self.directions["left"]
                else self.directions["down"]
            )
            self.current_row = self.direction

    def select_frame_row(self):
        if self.up:
            self.current_row = 5
        elif self.down:
            self.current_row = 3
        elif self.left:
            self.current_row, self.horizontal_flip = 4, True
        elif self.right:
            self.current_row, self.horizontal_flip = 4, False

    def update_player_pos(self):
        dx = dy = 0

        # Movement logic
        dy -= self.speed if self.up else 0
        dy += self.speed if self.down else 0
        dx += self.speed if self.right else 0
        dx -= self.speed if self.left else 0

        # Diagonal movement adjustment (normalize movement)
        if dx and dy:
            speed_adjust = 1 / (2**0.5)
            dx *= speed_adjust
            dy *= speed_adjust

        self.x += dx
        self.y += dy

        

    def select_frame(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > self.frame_delay:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(
                self.animation.frames[self.current_row]
            )

    def draw_frame(self, game):
        frame = self.animation.frames[self.current_row][self.current_frame]
        if self.horizontal_flip:
            frame = pygame.transform.flip(frame, True, False)
        game.screen.blit(frame, (self.x, self.y))
