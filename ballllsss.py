import pygame 
from random import *
pygame.init()
bg = (100,0,255)
clock = pygame.time.Clock()
speed_x = 3 
speed_y = 3
clock.tick(40)
window = pygame.display.set_mode((500,500))
box_color = (100,255,0)
window.fill(bg)
pygame.display.update()
win = False
class area():
    def __init__(self,x=0,y=0,width=10,height=10,color = None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color 
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def outline(self,frame_color,thickness):
        pygame.draw,rect(window,frame_color,self.rect,thickness)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
class picture(area):
    def __init__(self,filename,x=0,y=0,width=10,height=10):
        area.__init__(self,x=x,y=y,width=width,height=height,color = None)
        self.image = pygame.image.load(filename)
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
ball = picture('meatball.png',160,200,50,50)
pf = picture('meatball.png', 200, 300,100,30)
cool_bg = picture('meatball.png',0,0,5,5)
lost = picture('meatball.png',0,0,5,5)
won = picture('meatball.png',0,0,5,5)
start_x = 5
start_y = 5
cc = 9
move_right = False
move_left = False
cool_bg.draw()
enemies = []
for i in range(3):
    y = start_y + (55*i)
    x = start_x + (27.5*i)
    for i in range(cc):
        d = picture('meatball.png', x,y,50,50)
        enemies.append(d)
        d.draw()
        x+=55
        pygame.display.update()
    cc = cc-1
pygame.display.update()
game_over = False
while not game_over:
    cool_bg.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        if pf.rect.x < 410:
            pf.rect.x+=5
    if move_left:
        if pf.rect.x > 0:
            pf.rect.x = pf.rect.x-5
    for m in enemies:
        m.draw()
    pf.draw()
    ball.draw()
    ball.rect.x+=speed_x
    ball.rect.y+=speed_y
    if ball.colliderect(pf.rect):
        speed_y *= -1
    for m in enemies:
        if ball.colliderect(m.rect) and enemies != []:
            enemies.remove(m)
            speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= - 1
    if ball.rect.y < 0:
        speed_y *= - 1
    if ball.rect.y >= 300:
        game_over = True
    if enemies == []:
        game_over = True
        win = True
    clock.tick(40)
    pygame.display.update()
if game_over == True:
    lost.draw()
    pygame.display.update()
if game_over == True and win == True:
    won.draw()
    pygame.display.update()
