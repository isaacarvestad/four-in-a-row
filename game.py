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
        self.pieceSpacing = 10

        self.cursorColumn = 3
        self.cursorWidth = 30
        self.cursorHeight = 30
        self.cursorColor = (128, 128, 128)

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
        boardWidth = self.board.columns * (self.pieceWidth + self.pieceSpacing)
        boardHeight = self.board.rows * (self.pieceHeight + self.pieceSpacing)

        xStart = self.screenWidth/2 - boardWidth/2
        yStart = self.screenHeight/2 - boardHeight/2
        
        for x in range(self.board.columns):
            for y in range(self.board.rows):
                xPosition = xStart + x*(self.pieceWidth+self.pieceSpacing)
                yPosition = yStart + y*(self.pieceHeight+self.pieceSpacing)
                pygame.draw.rect(screen, (0,0,0), (xPosition, yPosition, self.pieceWidth, self.pieceHeight))

        xCursor = xStart + self.cursorColumn * (self.pieceWidth + self.pieceSpacing) + (self.pieceWidth - self.cursorWidth)/2
        yCursor = yStart - self.pieceHeight + (self.pieceHeight - self.cursorHeight)/2
        pygame.draw.rect(screen, self.cursorColor, (xCursor, yCursor, self.cursorWidth, self.cursorHeight))

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
