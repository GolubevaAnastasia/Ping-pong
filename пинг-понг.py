#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,s1,s2):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (s1, s2))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y+=self.speed        
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y+=self.speed       

window=display.set_mode((700, 500)) 
display.set_caption('pygame window')
ball=GameSprite('ball.png', 150, 20, 0, 65, 65)
sprite1=Player("rac.png", 600, 350, 7, 90, 100)
sprite2=Player("rac.png", 5, 40, 7, 90, 100)
clock=time.Clock()
FPS=60
game=True
finish=False
speed_x=3
speed_y=3
font.init()
font=font.Font(None, 66)
win1=font.render('Выиграл первый игрок', True, (255, 215, 0))
win2=font.render('Выиграл второй игрок', True, (255, 215, 0))
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if not finish:
        window.fill((124, 205, 124))
        ball.reset()
        sprite1.reset()
        sprite2.reset()
        sprite1.update_r()
        sprite2.update_l()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y

        if ball.rect.y > 450 or ball.rect.y<0:
            speed_y*=-1
        if sprite.collide_rect(sprite1, ball) or sprite.collide_rect(sprite2, ball):
            speed_x*=-1
        if ball.rect.x<0:
            finish=True
            window.blit(win2, (100, 50))
        if ball.rect.x>600:
            finish=True
            window.blit(win1, (100, 50))

        display.update()
        clock.tick(60)
