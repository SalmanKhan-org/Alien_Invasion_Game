import pygame 
from pygame.sprite import Sprite
class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and sets its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('C:/Users/accaz/AlienInvasion/Game/Images/ship.bmp')
        DEFAULT_IMAGE_SIZE = (50,50)
        self.image = pygame.transform.scale(self.image,DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

        #Start each ship at he bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)