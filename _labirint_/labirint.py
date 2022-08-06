from pygame import *
clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load("GTA.mp3")
mixer.music.play()

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, player_speed):
            super().__init__()

            self.image = transform.scale(image.load(player_image), (65, 65))
            self.speed = player_speed

            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

    def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 770:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
       # draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.rect):#


#игровая сцена
win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("mashina.jpg"), (win_width, win_height))

#Персонажи игры
player = Player('anonymos.jpg', 5, win_height - 80, 4)
monster = Enemy('пудж1.jpg', win_width - 80, 280, 2)
final = GameSprite('bitcoin2.jpg', win_width - 120, win_height - 80, 0)
#стены
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 495, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 100, 400, 250, 10)
w5 = Wall(154, 205, 50, 750, 200, 10, 500)
w6 = Wall(154, 205, 50, 450, 295, 10, 500)
w7 = Wall(154, 205, 50, 200, 295, 250, 10)
w8 = Wall(154, 205, 0, 540, 35, 10, 570)
w9 = Wall(154, 205, 50, 550, 595, 110, 10)
w10 = Wall(154, 205, 0, 650, 35, 10, 570)
w11 = Wall(154, 205, 50, 650, 20, 450, 10)
w12 = Wall(154, 205, 50, 750, 120, 10, 500)
w13 = Wall(154, 205, 50, 750, 120, 150, 10)

font.init()
font = font.Font(None, 100)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

finish = False
game = True
while game:   
    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()


        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13):
            finish = True
            window.blit(lose, (150, 150))
            kick.play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (150, 150))
            money.play()

    clock.tick(FPS)
    display.update()