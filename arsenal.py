"""
Arsenal Module

This module contains the Arsenal module which manages the players
weaponary via bullet creation, deletion, and rendering.
"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """
    This is the arsenal class which is used to manage the players weaponary.

    Attributes:
        game(AlienInvasion): The main instance of the game.
        settings(Settings): The games settings.
        arsenal(pygame.sprite.group): A group to store and manage all active bullets.
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """
        Initialize the arsenal and its attributes

        Args:
            game (AlienInvasion): The main instance of the game
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """
        updates the position of the bullets and remove off screen bullets
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """
        Removes bullets that have gone off screen
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """
        draws/renders bullets
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """
        Fires a bullet if the max number of bullets on screen has not been reached

        Returns:
            bool: True if bullet fired, false if otherwise
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False