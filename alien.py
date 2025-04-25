"""
Alien Module

This module contains the alien class which handles alien...
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """
    A class representing an alien enemy

    Args:
        screen (pygame.Surface): The game screen where the alien is rendered.
        settings (Settings): The game settings.
        boundaries (pygame.rect): A rectangle that represents the screen boundaries.
        image (pygame.Surface): The image of the alien.
        rect (pygame.rect): The rectangle representing the alien.
        ####y (float): The bullets y coordinate.
    """
    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        """
        Initialize the alien and set its starting position.

        Args:
            game (AlienInvasion): The main game instance.
        """
        super().__init__()

        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #self.y = float(self.rect.y)

    def update(self):
        """
        updates alien position
        """
    pass

    def draw_alien(self):
        """
        Draw/render the alien
        """
        self.screen.blit(self.image, self.rect)