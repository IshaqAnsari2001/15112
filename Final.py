import pygame
import random
import playerDictionary

# [right, left]
characters = playerDictionary.dictionary()
pygame.init()


floatingPlatforms = {}
floatingEnemies = {}

W = 1422
H = 790
win = pygame.display.set_mode((W,H))

pygame.display.set_caption("Oni And The Magical Forest")

# pygame.transform.flip(photo,True,False)
clock = pygame.time.Clock()

bg = pygame.image.load('morning.png').convert()
bg0 = pygame.image.load('morning.png').convert()
bg1 = pygame.image.load('evening.png').convert()
bg2 = pygame.image.load('night.png').convert()
pad = pygame.image.load('Pad 1.png').convert()
WHITE = (255, 255, 255)
pad.set_colorkey((0,0,0))


    
class MC():
    
    walkRight = characters["Godly Knight"][0]
    walkLeft = characters["Godly Knight"][1]
    idle = characters["Godly Knight"][2]
    
    def __init__(self,x,y,width,height,floatingPlatforms):
        
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.relativeHeroX = self.x - (self.width // 2)
        self.relativeHeroY = self.y - (self.height // 2)
        
        self.vel = 8
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 11
        self.standing = True
        self.onplatform = False
        self.neg = 0
        self.health = 10
        self.mana = 10
        self.hitbox = (self.x + 17, self.y + 11, 95, 110)
        self.i = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False
            
        elif keys[pygame.K_RIGHT] and self.x < W - self.width - self.vel:
            
            self.x += self.vel
            self.right = True
            self.left = False
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0
        
        if not (self.isJump):
            if keys[pygame.K_UP]:
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -11:
                self.neg = 1
                if self.jumpCount < 0:
                    self.neg = 0
                self.y -= ((self.jumpCount ** 2) * 0.5 * self.neg) 
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 11

    def gravity(self):
        #How to implement gravity
        if self.onplatform == False:
            self.y += 8.0
            
    def draw(self, win):
        
        if self.walkCount + 1 >= 16:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount//4], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//4], (self.x,self.y))
                self.walkCount +=1
        else:
            win.blit(self.idle[self.walkCount//4], (self.x,self.y))
            self.walkCount +=1

        pygame.draw.rect(win, (255,165,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10))
        pygame.draw.rect(win, (255,255,0), (self.hitbox[0], self.hitbox[1] - 20, 100 - round((5.15 * (10 - self.mana))), 10))
        
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 40, 100, 10))
        pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 40, 100 - round((10.0 * (10 - self.health))), 10))
        self.hitbox = (self.x + 10, self.y + 11, 95, 110)
        #pygame.draw.rect(win, (0,0,255), self.hitbox,2)

    def platform_check(self,floatingPlatforms):

        p1 = floatingPlatforms["platform 1"]
        if self.x + 90 >= p1.startX and self.x + 30 <= p1.endX:
            if self.y >= p1.startY - 110 and self.y <= p1.startY - 100:
                self.y = p1.startY - 110
                self.onplatform = True
        else:
            self.onplatform = False
            p2 = floatingPlatforms["platform 2"]
            if self.x + 90 >= p2.startX and self.x + 30 <= p2.endX:
                if self.y >= p2.startY - 110 and self.y <= p2.startY - 100:
                    self.onplatform = True
            else:
                self.onplatform = False
                p3 = floatingPlatforms["platform 3"]
                if self.x + 90 >= p3.startX and self.x + 30<= p3.endX:
                    if self.y >= p3.startY - 110 and self.y <= p3.startY - 100:
                        self.onplatform = True
                else:
                    self.onplatform = False 
                    p4 = floatingPlatforms["platform 4"]
                    if self.x + 90 >= p4.startX and self.x + 30 <= p4.endX:
                        if self.y >= p4.startY - 110 and self.y <= p4.startY - 100:
                            self.onplatform = True
                    else:
                        self.onplatform = False            
                        p5 = floatingPlatforms["platform 5"]
                        if self.x + 90 >= p5.startX and self.x + 30 <= p5.endX:
                            if self.y >= p5.startY - 110 and self.y <= p5.startY - 100:
                                self.onplatform = True
                        else:
                            self.onplatform = False

    def hit(self):
        self.health -= 2
        
        if self.health <= 0:
            self.health = 0
            print("Game over")
            
class Enemy():
    
    walkRight = characters["Evil Knight"][0]
    walkLeft = characters["Evil Knight"][1]
    die = characters["Evil Knight"][2]

    def __init__(self, x, y, width, height, name, floatingPlatforms):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = self.x + 250
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 4
        self.facing = 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 20
        self.visible = True
        self.platformName = name
        self.deathcount = 0

    def update(self):

        p = floatingPlatforms[self.platformName]
        if p.isout:
            self.x = p.startX
            self.y = p.startY - self.height

        if self.x + self.vel + (self.width//1.5) >= p.endX:
            self.facing = -1
            self.vel *= self.facing

        if self.x + self.vel + (self.width//2) < p.startX:
            self.facing = -1
            self.vel *= self.facing

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //4], (self.x, self.y))
                self.walkCount += 1
            if self.vel < 0:
                win.blit(self.walkLeft[self.walkCount //4], (self.x, self.y))
                self.walkCount += 1

        
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10))
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 100 - round((5.0 * (20 - self.health))), 10))
            self.hitbox = (self.x + 10, self.y , 95, 110)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel + (self.width//2) < W + 350:
                self.facing = 1
                self.vel = self.vel * self.facing
                self.x += self.vel
            else:
                self.facing = -1
                self.vel = self.vel * self.facing
                self.walkCount = 0
        else:
            if self.x - self.vel > -750:
                self.facing = 1
                self.vel *= self.facing
                self.x += self.vel
            else:
                self.facing = -1
                self.vel = self.vel * self.facing
                self.walkCount = 0

    def hit(self):
        
        if self.health > 0:
            self.health -= 8
            
        if self.health <= 0:
            self.visible = False
                

class projectile(MC):
    
    ballLeft = characters["Godly Knife"][1]
    ballRight = characters["Godly Knife"][0]
    
    def __init__(self,x,y,radius,color,ballfacing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.ballfacing = ballfacing
        self.vel = 6 * self.ballfacing
        self.moveCount = 0

    def draw(self,win):
        
        if self.moveCount + 1 >= 12:
            self.moveCount = 0
        if self.ballfacing == 1:  # facing right
            win.blit(self.ballRight[self.moveCount//4], (self.x - 105,self.y - 25))
            self.moveCount +=1
        else: # facing left
            win.blit(self.ballLeft[self.moveCount//4], (self.x - 25,self.y - 25))
            self.moveCount +=1
            
        #pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

            
class gameVariables():
    def __init__(self):

        # HERO CONFIG:
        self.heroX = 0
        self.heroY = 50 
        self.heroWidth = 95
        self.heroHeight = 110
        self.relativeHeroX = self.heroX - (self.heroWidth // 2)
        self.relativeHeroY = self.heroY - (self.heroHeight) - 5

class platformSet1():
    
    def __init__(self, startX, startY, win, floatingPlatforms,name,pad):

        self.name = name
        self.startX = startX
        self.startY = startY
        self.endX = 350 + self.startX
        self.endY = self.startY
        self.vel = -2
        self.i = 0
        self.j = 0
        self.index = 0
        self.photo = pad
        self.isout = False

    def draw_platform(self,win):
        #win.blit(bg, (rel_x - bg.get_rect().width, 0))
        win.blit(self.photo,(self.startX,self.startY - 15))
        #pygame.draw.rect(win, (255,0,0),(self.startX , self.startY, 350, 15))

    def update_platform(self):
        self.startX += self.vel
        self.endX += self.vel
        
    def create_platform(self,floatingPlatforms):
        
        possiblePlatform = [160,278,450,622]
        possibleValues = [-1,1]

        if (self.startX == -10):
            if self.name == "platform 1":
                p5 = floatingPlatforms["platform 5"]
                if p5.startY != 622:
                    self.index = possiblePlatform.index(p5.startY)
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
                    
            if self.name == "platform 2":
                p1 = floatingPlatforms["platform 1"]
                if p1.startY != 622:
                    self.index = possiblePlatform.index(p1.startY)
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
                    
            if self.name == "platform 3":
                p2 = floatingPlatforms["platform 2"]
                if p2.startY != 622:
                    self.index = possiblePlatform.index(p2.startY)
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
                    
            if self.name == "platform 4":
                p3 = floatingPlatforms["platform 3"]
                if p3.startY != 622:
                    self.index = possiblePlatform.index(p3.startY)
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
                    
            if self.name == "platform 5":
                p4 = floatingPlatforms["platform 4"]
                if p4.startY != 622:
                    self.index = possiblePlatform.index(p4.startY)
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
            
        if (self.endX <= 0):
            self.isout = True
            self.startX = 1900
            self.startY = possiblePlatform[self.i]
            self.endX = 350 + self.startX
            self.endY = self.startY
        else:
            self.isout = False
            
def redrawGameWindow():
    
    p1.draw_platform(win)
    p2.draw_platform(win)
    p3.draw_platform(win)
    p4.draw_platform(win)
    p5.draw_platform(win)
    Hero.draw(win)
    enemy.draw(win)
    enemy1.draw(win)
    start = -1
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()

def scrolling(x, count, bg, bg0, bg1, bg2):
    rel_x = x % bg.get_rect().width
    if (rel_x >= 0 and rel_x <= 5):
        count += 1
    count = count % 11
    if((count) <= 4):
        bg = bg0
    elif((count) > 4 and count <= 7):
        bg = bg1
    elif((count) > 7 and count <= 10):
        bg = bg2
    win.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < W:
            win.blit(bg, (rel_x, 0))
    

def bulletCollision(Hero,enemy,bullets,bulletCount):
    
    if bulletCount > 0:
        bulletCount += 1
    if bulletCount > 3:
        bulletCount = 0
    
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                bullets.pop(bullets.index(bullet))
                
                
        if bullet.x < W and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
        
    if keys[pygame.K_SPACE] and bulletCount == 0:
        if Hero.left:
            ballfacing = -1
        else:
            ballfacing = 1
            
        if len(bullets) < 1 :
            bullets.append(projectile(round(Hero.x + Hero.width //2), round(Hero.y + Hero.height//2), 6, (255,0,0), ballfacing))
        bulletCount = 1       
        
#mainloop
font = pygame.font.SysFont('comicsans', 40, True)
#()
game = gameVariables()

#(x,y,width,height)
Hero = MC(game.heroX, game.relativeHeroY, game.heroWidth, game.heroHeight,floatingPlatforms)

p1 = platformSet1(0,160,win,floatingPlatforms,"platform 1", pad)
floatingPlatforms["platform 1"] = p1
p2 = platformSet1(450,450,win,floatingPlatforms,"platform 2", pad)
floatingPlatforms["platform 2"] = p2
p3 = platformSet1(900,278,win,floatingPlatforms,"platform 3", pad)
floatingPlatforms["platform 3"] = p3
p4 = platformSet1(1350,622,win,floatingPlatforms,"platform 4", pad)
floatingPlatforms["platform 4"] = p4
p5 = platformSet1(1800,450,win,floatingPlatforms,"platform 5", pad)
floatingPlatforms["platform 5"] = p5

#self.relativeEnemyX = self.enemyX - (self.enemyWidth // 2)
#self.relativePathEnd = self.enemyPathEnd - self.enemyWidth
#
enemy = Enemy(900, (278 - 100), 110, 95, "platform 3", floatingPlatforms)
enemy1 = Enemy(1800, (450 - 100), 110, 95, "platform 5", floatingPlatforms)

bulletCount = 0
bullets = []
platformList = []
platforms = []
scrollCount = 0
scrollX = 0
i = 0
   
condition = True
condition1 = True

Program = True
while Program:
    
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Program = False

    keys = pygame.key.get_pressed()

    scrolling(scrollX, scrollCount, bg, bg0, bg1, bg2)
    scrollX -= 3
 
    Hero.movement()
  
    Hero.gravity()
    Hero.platform_check(floatingPlatforms)

    enemy.update()
    enemy1.update()
    
    p1.update_platform()
    p2.update_platform()
    p3.update_platform()
    p4.update_platform()
    p5.update_platform()

    p1.create_platform(floatingPlatforms)
    p2.create_platform(floatingPlatforms)
    p3.create_platform(floatingPlatforms)
    p4.create_platform(floatingPlatforms)
    p5.create_platform(floatingPlatforms)
    
    bulletCollision(Hero,enemy,bullets,bulletCount)
    bulletCollision(Hero,enemy1,bullets,bulletCount)
    
    if Hero.x + Hero.width >= enemy.x and Hero.x + Hero.width <= enemy.x + enemy.width:
        if (Hero.y + 10 >= enemy.y or Hero.y - 5 <= enemy.y) and condition:
            Hero.hit()
            condition = False
                
    elif (Hero.x + Hero.width < enemy.x or Hero.x + Hero.width > enemy.x + enemy.width or Hero.y < enemy.y ) and condition == False:
        condition = True
        
    if Hero.x + Hero.width >= enemy1.x and Hero.x + Hero.width <= enemy1.x + enemy1.width:
        if (Hero.y + 10 >= enemy1.y or Hero.y - 5 <= enemy1.y) and condition1:
            Hero.hit()
            condition1 = False
                
    elif (Hero.x + Hero.width < enemy1.x or Hero.x + Hero.width > enemy1.x + enemy1.width or Hero.y < enemy1.y ) and condition1 == False:
        condition1 = True

    # GAME OVER IF YOU FALL BELOW THE SCREEN
    if (Hero.y + Hero.height//2 >= H):
        Program = False
     
    redrawGameWindow()
pygame.quit()
