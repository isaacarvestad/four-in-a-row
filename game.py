import pygame, sys, random

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
                if event.key == pygame.K_LEFT:
                    if self.cursorColumn > 0:
                        self.cursorColumn -= 1
                if event.key == pygame.K_RIGHT:
                    if self.cursorColumn < 6:
                        self.cursorColumn += 1
                if event.key == pygame.K_SPACE:
                    self.board.addPiece(self.cursorColumn, 1)
                    self.board.addPiece(random.randint(0,6), 2)
                    
        return True

    def render(self, screen):
        self.screen.fill((255,255,255))
        
        boardWidth = self.board.columns * (self.pieceWidth + self.pieceSpacing)
        boardHeight = self.board.rows * (self.pieceHeight + self.pieceSpacing)

        xStart = self.screenWidth/2 - boardWidth/2
        yStart = self.screenHeight/2 - boardHeight/2
        
        for x in range(self.board.columns):
            for y in range(self.board.rows):
                xPosition = xStart + x*(self.pieceWidth+self.pieceSpacing)
                yPosition = yStart + y*(self.pieceHeight+self.pieceSpacing)
                pieceColor = (0,0,0)
                if self.board.boardMatrix.item((y, x)) == 1:
                    pieceColor = (255,0,0)
                elif self.board.boardMatrix.item((y, x)) == 2:
                    pieceColor = (0,255,0)
                    
                pygame.draw.rect(screen, pieceColor, (xPosition, yPosition, self.pieceWidth, self.pieceHeight))

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
