import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and sets its rect attributes
        self.image = pygame.image.load('C:/Users/accaz/AlienInvasion/Game/Images/alien.bmp')
        DEFAULT_IMAGE_SIZE = (40,40)
        self.image = pygame.transform.scale(self.image,DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        #Start each new alien at the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to write"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """Return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
