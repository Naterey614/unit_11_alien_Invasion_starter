"""
Ship Module

This module contains the ship class, which is the players ship.
The ship moves left and right and fires bullets.
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """
    This class is the ship class, which represents the players ship.

    Attributes:
        game (AlienInvasion): The main game instance.
        settings (Settings): The game settings.
        screen (pygame.Surface): The game screen.
        boundaries (pygame.Rect): The boundaries of the game screen.
        image (pygame.Surface): The ship's image.
        rect (pygame.Rect): The rectangle representing the ship's position.
        moving_right (bool): Whether the ship is moving to the right.
        moving_left (bool): Whether the ship is moving to the left.
        x (float): The ship's x-coordinate for precise movement.
        arsenal (Arsenal): The ship's arsenal for managing bullets.
    """
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """
        Initialization of ship and its attributes.

        Args:
            game (AlienInvasion): The main instance of the game.
            arsenal (Arsenal): The weapon management system script.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self) -> None:
        """
        updates ships weaponary and positioning
        """
        #updating position of ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        moves the ship to the left or right when the left or right arrow keys are pressed
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right == True and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left == True and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self) -> None:
        """
        draws/renders the ship and the ships arsenal
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """
        Fires a bullet

        Returns:
            bool: True if bullet can fire, false if otherwise
        """
        return self.arsenal.fire_bullet()