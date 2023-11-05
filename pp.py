from random import randint
from pygame import *
win_height = 500
win_width = 700


class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        #self.image_r = transform.rotate(self.image, randint(50,180))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()   
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y  < win_width - 0:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()  
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y  < win_width - 0:
            self.rect.y += self.speed

'''
class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if self.rect.y >= win_height or self.rect.y <= 0:
            self.rect.y *= -1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            self.rect.x -= self.speed
        if sprite.collide_rect(ball, wall1, False, False):
            self.rect.y *= -1

'''

        


clock = time.Clock()
FPS = 60

window = display.set_mode((700,500))
display.set_caption('Настольный теннис')

background = transform.scale(image.load('ppbck.jpg'),(700, 500))

player1 = Player1('rocket.png', 640, 220, 5, 65, 65)
player2 = Player2('rocket.png', -5, 220, 5, 65, 65)
ball = GameSprite('ball.png', 320, 150, 10, 65, 65)
wall1 = GameSprite('wall.png', -80, 440, 5, 850, 100)


game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 5
speed_y = 5

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        ball.rect.x += speed_x
        ball.rect.x += speed_y
      
        
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1        
        player1.update()
        player2.update()
        player1.reset()
        player2.reset()
        ball.update()
        ball.reset()
        wall1.update()
        wall1.reset()

    display.update()
    clock.tick(FPS)