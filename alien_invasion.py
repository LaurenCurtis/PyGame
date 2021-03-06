

import pygame
from settings import Settings
class AlienInvasion:
    #Overall class to manage game assets and behavior"
    def __init__(self):
        #Initialize game and create resource 
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #set the background color 
        self.bg_color = (230,230,230)
    def run_game(self):
        self.screen.fill(self.settings.bg_color)
        #Start the main loop for the game
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
                #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '_main_':
    #Make a game instance, and run
    ai = AlienInvasion()
    ai.run_game()