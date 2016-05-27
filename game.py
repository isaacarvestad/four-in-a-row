import pygame, sys

from board import Board

"""
A simple four in a row game.

Author: Isaac Arvestad
"""
class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((600,600))
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255,255,255))
        self.background = self.background.convert()
        
        self.screen.blit(self.background, (0,0))
        
        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]
        
        self.board = Board(7, 7)
        self.pieceWidth = 50
        self.pieceHeight = 50

    def update(self):
        "Handle input."
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def render(self, screen):
        for x in range(self.board.columns):
            for y in range(self.board.rows):
                pygame.draw.rect(screen, (0,0,0), (x*self.pieceWidth, y*self.pieceHeight, self.pieceWidth, self.pieceHeight))

    "Starts the game."
    def start(self):
        while True:
            if not self.update():
                break

            self.render(self.screen)
            
            pygame.display.update()
        self.exit()

    def exit(self):
        pygame.quit()
        sys.exit()

game = Game()
game.start()
