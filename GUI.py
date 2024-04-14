import pygame as pg
import sys
import time
from random import randint,choice

from Sudoku import solve, isValid,print_board

pg.init()
screen_size = 750,750
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Sudoku")
clock =pg.time.Clock()
board = [[0 for _ in range(9)] for _ in range(9)]
sprites = [[None for _ in range(9)] for _ in range(9)]
win = True
running = True
#Fonts
num_font = pg.font.Font(None, 40)
win_font = pg.font.Font(None, 100)
snum_font = pg.font.Font(None, 10)


class Rect(pg.sprite.Sprite):
    def __init__(self,x,y,num,snum):
        super().__init__()
        self.image = pg.Surface((80,80))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill(pg.Color("white")) 
        self.x = x
        self.y = y
        self.number = num
        self.snum = snum
    def update(self):
        if(self.number != 0):
            number = num_font.render(f'{self.number}',False,pg.Color("black"))
            number_rect = number.get_rect(center = (self.x+40,self.y+40))
            screen.blit(number, number_rect)
    def fill(self):
        self.image.fill(pg.Color("gray"))
    def re_fill(self):
        self.image.fill(pg.Color("white"))
    def draw(self,screen):
        if self.snum != 0 :
            number = num_font.render(f'{self.number}',False,pg.Color("black"))
            number_rect = number.get_rect(center = (self.x+5,self.y+5))
        

class FixedRect(Rect):
    def __init__(self, x, y, constant,sconstant):
        super().__init__(x,y,constant,sconstant)
        self.constant = constant
        self._number = self.number
        self.image.fill(pg.Color("yellow"))
    def fill(self):
        self.image.fill(pg.Color("yellow"))
    def re_fill(self):
        self.image.fill(pg.Color("yellow"))


#draw grid_lines
def draw_background():
    
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15,15,720,720),10)
    i =1
    while(i*80)<720:
        if(i%3 == 0):
            pg.draw.line(screen,pg.Color("black"),((i*80)+15, 15),((i*80)+15,735), 15)
            pg.draw.line(screen,pg.Color("black"),(15, (i*80)+15),(735, (i*80)+15), 15)
        else:
            pg.draw.line(screen,pg.Color("black"),((i*80)+15, 15),((i*80)+15,735), 5)
            pg.draw.line(screen,pg.Color("black"),(15, (i*80)+15),(735, (i*80)+15), 5)
        i += 1


#Add rect number
rect_group = pg.sprite.Group()
for row in range(9):
    for column in range(9):
            num = choice([0,0,0,randint(1, 9)])
            if(isValid(board, num, row, column)):
                rect_group.add(FixedRect(15 + (80 * column), 15 + (80 * row), num,0))
                board[row][column] = num
            else:
                rect_group.add(Rect(15 + (80 * column), 15 + (80 * row), 0, 0))
                board[row][column] = 0
sprites = rect_group.sprites()
print_board(board)
print(" ")
print(" ")
print(" ")
solve(board,0,0)
print_board(board)

#Iteration for sprites[i]
i=0
#Active loop
while True:
    for event in pg.event.get():
        if running:
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                
                if i != -1 and sprites[i] is not None:  # Check if a sprite is selected
                    if event.key in [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]:
                        if isinstance(sprites[i],FixedRect):
                            pass
                        else:
                            number = int(pg.key.name(event.key))  # Get the number from the key
                            sprites[i].number = number  # Set the number for the selected sprite
                            for j in range(9):
                                sprites[int(i/9)*9 +j].fill()
                                sprites[int(i%9) + 9*j].fill()
                            board[int(i/9)][int(i%9)] = number #assign number into board
                if event.key == pg.K_RETURN:
                    running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                # Check if any Rect sprite was clicked
                    for j in range(9):
                        if sprites[int(i/9)*9 +j] != FixedRect and sprites[int(i%9) + 9*j] != FixedRect:
                            sprites[int(i/9)*9 +j].re_fill()
                            sprites[int(i%9) + 9*j].re_fill()
                    i = 0   
                    for i in range(81): 
                        if sprites[i].rect.collidepoint(event.pos):
                            break        
            
            # Draw the background
            screen.fill(pg.Color("White"))
            # Update and draw the sprites
            rect_group.draw(screen)
            rect_group.update()
            draw_background()
        else:
            screen.fill(pg.Color("white"))
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                running = True
            for k in range(81):
                if sprites[k].number != board[int(k/9)][int(k%9)]:
                    win = False
                    break
            if win:
                win_surface = win_font.render('You Win',False,'Red')
            else:
                win_surface = win_font.render('You Lose',False,'Red')
            win_rect = win_surface.get_rect(center = (750/2,750/2))
            screen.blit(win_surface,win_rect)
    pg.display.update()
    clock.tick(60)


    

