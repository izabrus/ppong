from random import *
from pygame import *
from time import time as timer
from time import sleep
mixer.init()
mixer.music.load('main_theme.ogg')
mixer.music.play()
fire = mixer.Sound('vine-boom-.ogg')
window = display.set_mode((700,500))
display.set_caption('Шутер')
clock = time.Clock()
FPS = 60
x1 = 100
y1 = 300
x2 = 520
reloading = False
y2 = 250
font.init()
lost = 0 
score = 0
font1 = font.SysFont(None,36)
font2 = font.SysFont(None,36)
font3 = font.SysFont(None,100)
font4 = font.SysFont(None,100)
lose_text = font1.render('Пропущено: '+str(lost),1,(255,255,255))
win_text = font3.render('WIN',1,(0,255,0))
lost1 = font4.render('LOSE',1,(255,0,0))
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
class Main(GameSprite):
     def __init__(self,p_image,p_x,p_y,p_speed,reload_counter,reloading):
          super().__init__(p_image,p_x,p_y,p_speed)
          self.reload_counter = 0 
     def update(self):
          key_pressed = key.get_pressed()
          if key_pressed[K_a] and self.rect.x>5:
               self.rect.x-=self.p_speed
          if key_pressed[K_d] and self.rect.x<635:
               self.rect.x+=self.p_speed
     def shoot(self):
          key_pressed = key.get_pressed()
          if key_pressed[K_w]:
               if reloading == False:
                    self.reload_counter +=1
                    zamn = Projectile('zamn.jpg',self.rect.centerx,self.rect.top,-15)
                    bullets.add(zamn)
                    fire.play()
class Villian(GameSprite):
     def __init__(self,p_image,p_x,p_y,p_speed):
          super().__init__(p_image,p_x,p_y,p_speed)
          self.dir = 'down'
     def update(self):
          self.rect.y+=self.p_speed
          global lost
          if self.rect.y > 500:
               self.rect.x=randint(80,620)
               self.rect.y=0
               lost+=1
     def killing(self):
          self.kill()
class Projectile(GameSprite):
     def __init__(self,p_image,p_x,p_y,p_speed):
          super().__init__(p_image,p_x,p_y,p_speed)
          self.dir = 'left'
     def update(self):
          self.rect.y += self.p_speed
          if self.rect.y < 0:
              self.kill()
background = transform.scale(image.load('doomspire_bg.jpg'),(700,500))
v_x = 30
main_char = Main('goofycat.jpg',310,420,8,0,False)
#задай фон сцены
enemies = []
finish = False
game = True
amogus = 0
speed_v = randint(2,4)
a = timer()
bullets = sprite.Group()
ballers = sprite.Group()
players = sprite.Group()
meatballs = sprite.Group()
players.add(main_char)
lifes = 3 
for b in range(1,6):
     v_x1 = randint(0,400)
     speed_v = randint(2,4)
     baller = Villian('baller.png',v_x1,30,speed_v)
     ballers.add(baller)
for k in range(1,6):
     v_x1 = randint(0,400)
     speed_v = randint(2,4)
     meatball = Villian('meatball.png',v_x1,30,speed_v)
     meatballs.add(meatball)
while game:
     for i in event.get():
          if i.type==QUIT:
               game=False
          elif i.type == KEYDOWN:
               if i.key == K_r:
                    window.blit(background,(0,0))
                    for b in ballers:
                         b.kill()
                    for m in bullets:
                         m.kill()
                    for j in meatballs:
                         j.kill()
                    for b in range(1,6):
                         v_x1 = randint(0,400)
                         speed_v = randint(2,4)
                         baller = Villian('baller.png',v_x1,30,speed_v)
                         ballers.add(baller)
                    for k in range(1,6):
                         v_x1 = randint(0,400)
                         speed_v = randint(2,4)
                         meatball = Villian('meatball.png',v_x1,30,speed_v)
                         meatballs.add(meatball)
                    ballers.draw(window)
                    bullets.draw(window)
                    players.draw(window)
                    meatballs.draw(window)
                    score = 0
                    lifes = 3 
                    lost = 0 
                    finish = False
     if finish == False:
          window.blit(background,(0,0))
          text = font2.render('Счет:'+str(score),1,(255,255,255))
          amogus_font = font2.render('Жизни:'+str(lifes),1,(255,255,255))
          lose_text = font2.render('Пропущено: '+str(lost),1,(255,255,255))
          reload_text = font2.render('Перезарядка...',1,(0,0,255))
          window.blit(text,(10,20))
          window.blit(lose_text,(10,40))
          window.blit(amogus_font,(10,60))
          ballers.update()
          ballers.draw(window)
          bullets.update()
          bullets.draw(window)
          meatballs.draw(window)
          meatballs.update()
          main_char.update()
          main_char.reset()
          if main_char.reload_counter < 10:
               main_char.shoot()
          if main_char.reload_counter > 10:
               b = timer()
               reloading = True 
               window.blit(reload_text,(250,185))
               if b-a>3:
                    reloading = False
                    main_char.reload_counter = 0
                    a = timer()
          main_char.shoot()
          hits = sprite.groupcollide(ballers, bullets, True, True)
          hits1 = sprite.groupcollide(players, ballers, False, True)
          hits2 = sprite.groupcollide(players,meatballs,False,True)
          hits3 = sprite.groupcollide(meatballs,bullets,False,True)
          if hits:
               v_x1 = randint(0,400)
               speed_v = randint(2,4)
               baller = Villian('baller.png',v_x1,30,speed_v)
               ballers.add(baller)
               score +=1 
          if hits1:
               lifes-=1
               v_x1 = randint(0,400)
               speed_v = randint(2,4)
               baller = Villian('baller.png',v_x1,30,speed_v)
               ballers.add(baller)
               score +=1 
          if hits2:
               lifes-=1
               v_x1 = randint(0,400)
               speed_v = randint(2,4)
               meatball = Villian('meatball.png',v_x1,30,speed_v)
               meatballs.add(meatball)
          if score == 10:
               window.blit(win_text,(250,185))
               finish = True
          if lost >= 10:
               window.blit(lost1,(250,185))
               finish = True
          if lifes <= 0:
               window.blit(lost1,(250,185))
               finish = True
     display.update()
     clock.tick(FPS)