from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

display.set_caption("ping-pong")
window = display.set_mode((700, 500))
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

player_1 = Player('rocket.png', 600, 10, 80, 100, 10)
player_2 = Player('rocket.png', 10, 10, 80, 100, 10)

FPS = 60
clock = time.Clock()

finish = False
run = True    
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
        player_1.update_1()
        player_2.update_2()
        player_1.reset()
        player_2.reset()
    clock.tick(FPS)
    display.update()