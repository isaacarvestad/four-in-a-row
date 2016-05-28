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
        
        self.screen_width = self.screen.get_size()[0]
        self.screen_height = self.screen.get_size()[1]
        
        self.board = Board(7, 7)
        self.piece_width = 50
        self.piece_height = 50
        self.piece_spacing = 10

        self.cursor_column = 3
        self.cursor_width = 30
        self.cursor_height = 30
        self.cursor_color = (128, 128, 128)
        
    def update(self):
        "Handle input."
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_LEFT:
                    if self.cursor_column > 0:
                        self.cursor_column -= 1
                if event.key == pygame.K_RIGHT:
                    if self.cursor_column < 6:
                        self.cursor_column += 1
                if event.key == pygame.K_SPACE:
                    self.board.add_piece(self.cursor_column, 1)
                    self.board.add_piece(random.randint(0,6), 2)
                    
        return True

    def render(self, screen):
        self.screen.fill((255,255,255))
        
        board_width = self.board.columns * (self.piece_width + self.piece_spacing)
        board_height = self.board.rows * (self.piece_height + self.piece_spacing)

        x_start = self.screen_width/2 - board_width/2
        y_start = self.screen_height/2 - board_height/2
        
        for x in range(self.board.columns):
            for y in range(self.board.rows):
                x_position = x_start + x*(self.piece_width+self.piece_spacing)
                y_position = y_start + y*(self.piece_height+self.piece_spacing)
                piece_color = (0,0,0)
                if self.board.matrix.item((y, x)) == 1:
                    piece_color = (255,0,0)
                elif self.board.matrix.item((y, x)) == 2:
                    piece_color = (0,255,0)
                    
                pygame.draw.rect(screen, piece_color, (x_position, y_position, self.piece_width, self.piece_height))

        x_cursor = x_start + self.cursor_column * (self.piece_width + self.piece_spacing) + (self.piece_width - self.cursor_width)/2
        y_cursor = y_start - self.piece_height + (self.piece_height - self.cursor_height)/2
        pygame.draw.rect(screen, self.cursor_color, (x_cursor, y_cursor, self.cursor_width, self.cursor_height))

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
