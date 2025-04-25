"""
Settings Module

This module contains the settings class which has all of the settings for the Alien Invasion Game
"""

from pathlib import Path
class Settings:
    """
    Settings class stores all settings for the Alien Invasion game.

    Attributes:
        name (str): The name of the game.
        screen_w (int): The width of the game screen in pixels.
        screen_h (int): The height of the game screen in pixels.
        FPS (int): The target frames per second for the game.
        bg_file (Path): The file path to the background image.

        ship_file (Path): The file path to the ship image.
        ship_w (int): The width of the ship in pixels.
        ship_h (int): The height of the ship in pixels.
        ship_speed (int): The speed of the ship in pixels per frame.

        bullet_file (Path): The file path to the bullet image.
        laser_sound (Path): The file path to the laser sound effect.
        bullet_speed (int): The speed of bullets in pixels per frame.
        bullet_w (int): The width of bullets in pixels.
        bullet_l (int): The length of bullets in pixels.
        bullet_amount (int): The maximum number of bullets allowed on screen at once.
    """

    def __init__(self):
        """
        Initialize the game's settings.
        """

        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path().cwd() / 'Assets' / 'images' / 'starbasesnow.png'

        self.ship_file = Path().cwd() / 'Assets' / 'images' / 'Custom Ship.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        self.bullet_file = Path().cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path().cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_l = 80
        self.bullet_amount = 5

        self.alien_file = Path().cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2