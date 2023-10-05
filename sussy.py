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
          self.reload_counter = 0 
          self.p_speed_x = 3
          self.p_speed_y = 3
     def update(self):
          self.rect.y+=self.p_speed_y
          self.rect.x+=self.p_speed_x
     def colliderect(self,rect):
          return self.rect.colliderect(rect)  

player_1 = Main1('baller.png',300,30,10)
player_2 = Main2('baller.png',300,380,10)
meatball = ball('meatball.png',300,200,5)

while game:
     for i in event.get():
          if i.type==QUIT:
               game=False
     if finish == False:
          window.blit(background,(0,0))
          player_1.update()
          player_1.reset()
          player_2.update()         
          player_2.reset()  
          meatball.update()
          meatball.reset()
          if meatball.colliderect(player_1) or meatball.colliderect(player_2):
               meatball.p_speed_x *= -1
          if meatball.rect.x > 650 or meatball.rect.x < 10:
               meatball.p_speed_x *= - 1
          if meatball.rect.y > 450 or meatball.rect.y < 10:
               meatball.p_speed_y *= - 1
          display.update()
          clock.tick(FPS)