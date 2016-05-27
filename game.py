import pygame, sys

"""
A simple four in a row game.

Author: Isaac Arvestad
"""
class Game:
    def __init__(self):


    def update(self):
        "Handle input."
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                

    def render(self):


    "Starts the game."
    def start(self):
        while True:
            if not self.update():
                break

            self.render()
            
            pygame.display.update()
        self.exit()

    def exit(self):
        pygame.quit()
        sys.exit()
