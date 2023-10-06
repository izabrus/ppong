from random import *
from pygame import *
from time import time as timer
from time import sleep

mixer.init()
window = display.set_mode((700,500))
display.set_caption('PPong')
clock = time.Clock()
background = transform.scale(image.load('doomspire_bg.jpg'),(700,500))
game = True
finish = False
FPS = 60

font.init()
font3 = font.Font(None,100)
font4 = font.Font(None,100)
font5 = font.Font(None,100)
win_text_p1 = font3.render('1ST PLAYER WON',1,(0,255,0))
win_text_p2 = font4.render('2ND PLAYER WON',1,(0,255,0))
overtime_text = font5.render('OVERTIME',1,(255,0,0))

start_time = timer()
skibidi = False
showing_text = False

class GameSprite(sprite.Sprite):
     def __init__(self,p_image,p_x,p_y,p_speed):
          super().__init__()
          self.image = transform.scale(image.load(p_image),(65,65))
          self.p_speed = p_speed
          self.rect = self.image.get_rect()
          self.rect.x = p_x
          self.rect.y = p_y
          self.reload_counter = 0
     def reset(self):
          window.blit(self.image,(self.rect.x,self.rect.y))

class Main1(GameSprite):
     def __init__(self,p_image,p_x,p_y,p_speed):
          super().__init__(p_image,p_x,p_y,p_speed)
          self.reload_counter = 0 
     def update(self):
          key_pressed = key.get_pressed()
          if key_pressed[K_a] and self.rect.x>5:
               self.rect.x-=self.p_speed
          if key_pressed[K_d] and self.rect.x<635:
               self.rect.x+=self.p_speed

class Main2(GameSprite):
     def __init__(self,p_image,p_x,p_y,p_speed):
          super().__init__(p_image,p_x,p_y,p_speed)
          self.reload_counter = 0 
     def update(self):
          key_pressed = key.get_pressed()
          if key_pressed[K_LEFT] and self.rect.x>5:
               self.rect.x-=self.p_speed
          if key_pressed[K_RIGHT] and self.rect.x<635:
               self.rect.x+=self.p_speed 
                    
class ball(GameSprite):
     def __init__(self,p_image,p_x,p_y,p_speed):
          super().__init__(p_image,p_x,p_y,p_speed)
          self.p_speed_x = 3
          self.p_speed_y = 3
     def update(self):
          self.rect.y+=self.p_speed_y
          self.rect.x+=self.p_speed_x
     def colliderect(self,rect):
          return self.rect.colliderect(rect)  

player_1 = Main1('baller.png',300,30,10)
player_2 = Main2('baller.png',300,380,10)
meatball = ball('meatball.png',300,200,10)

while game:
     for i in event.get():
          if i.type==QUIT:
               game=False
          elif i.type == KEYDOWN:
               if i.key == K_r:
                    start_time = timer()
                    window.blit(background,(0,0))
                    player_1.kill()
                    player_2.kill()
                    meatball.kill()
                    player_1 = Main1('baller.png',300,30,10)
                    player_2 = Main2('baller.png',300,380,10)
                    meatball = ball('meatball.png',300,200,10)
                    meatball.p_speed_x = 3
                    meatball.p_speed_y = 3 
                    finish = False
                    showing_text = False
     if finish == False:
          amogus_time = timer()
          window.blit(background,(0,0))
          player_1.update()
          player_1.reset()
          player_2.update()         
          player_2.reset()  
          meatball.update()
          meatball.reset()
          if amogus_time - start_time >= 7 and showing_text == False:
               window.blit(overtime_text,(170,400))
               meatball.p_speed_x = 5
               meatball.p_speed_y = 5
               sleep(3)
               window.blit(background,(0,0))
               player_1.update()
               player_1.reset()
               player_2.update()         
               player_2.reset()  
               meatball.update()
               meatball.reset()
               skibidi = True
               showing_text = True
          if meatball.colliderect(player_1) or meatball.colliderect(player_2):
               meatball.p_speed_y *= -1
          if meatball.rect.x > 650 or meatball.rect.x < 10:
               meatball.p_speed_x *= - 1
               meatball.p_speed_y *= -1
          if meatball.rect.y > 450:
               if skibidi == False:
                    window.blit(background,(0,0))
                    window.blit(win_text_p1,(30,185))
                    finish = True
               if skibidi == True:
                    window.blit(background,(0,0))
                    window.blit(win_text_p1,(30,185))
                    finish = True
          if meatball.rect.y < 10:
               if skibidi == False:
                    window.blit(background,(0,0))
                    window.blit(win_text_p2,(30,185))
                    finish = True
               if skibidi == True:
                    window.blit(background,(0,0))
                    window.blit(win_text_p2,(30,185))
                    finish = True
          display.update()
          clock.tick(FPS)