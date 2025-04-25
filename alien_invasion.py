#module documentation, class doc, func doc, type hints
"""
Alien Invasion Game

This module contains the main game logic for the alien invasion game
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien

class AlienInvasion:
    """
    This class manages all of the game resources and behaviors

    Attributes:
        settings (Settings): The game settings.
        screen (pygame.Surface): The game screen.
        bg (pygame.Surface): The background image.
        running (bool): Whether the game is running.
        clock (pygame.time.Clock): The game clock.
        laser_sound (pygame.mixer.Sound): The sound effect for firing lasers.
        ship (Ship): The player's ship.
    """
    def __init__(self) -> None:
        """
        Initializes game and game resources.
        """

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

    
        self.ship = Ship(self, Arsenal(self))
        self.alien = Alien(self, 10, 10)

    def run_game(self) -> None:
        """
        contains the main game loop.
        """

        # Game loop
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self) -> None:
        """
            handles all rendering/drawing.
        """

        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien.draw_alien()
        pygame.display.flip()

    def _check_events(self) -> None:
        """
            handles user input events.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event) -> None:
        """
        handles key release events.

        Args:
            event (pygame.event.Event): Player input event
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event) -> None:
        """
        handles key press events.

        Args:
            event (pygame.event.Event): Player input event.
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.quit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()