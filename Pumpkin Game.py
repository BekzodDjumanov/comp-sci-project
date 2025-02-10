# Let's make a game gentleman...
import pygame
import time
import random

#citation list (note that this is not a key:value system)
citations = [
    "1: Vi, A. (2017). Pixel happy Halloween pumpkin stock illustrations. iStock. https://www.istockphoto.com/illustrations/pixel-happy-halloween-pumpkin",
    "2: X, A. (2018). Black silhouettes of grass. floral background. wild grass. grass borders silhouette. vector illustration stock vector. Adobe Stock. https://stock.adobe.com/images/Black-silhouettes-of-grass.-Floral-background.-Wild-grass.-Grass-borders-silhoue/558648725?as_campaign=TinEye&as_content=tineye_match",
    "3: P_Ang, P. (2015). Pixel art 8bit Moon icon with glowing light.8bit. stock vector. Adobe Stock. https://stock.adobe.com/images/pixel-art-8bit-moon-icon-with-glowing-light-8bit/286253186",
    "4: P2020, D. (2018). Spiky Ball. Pixilart. https://www.pixilart.com/art/spiky-ball-9e60cbb50e30729",
    "5: Marketplace, I. (2017). Download an 8-bit retro-styled pixel-art illustration of a Spooky Green Witch holding a magical Orange Potion. for Free. Vecteezy. https://www.vecteezy.com/png/27226464-an-8-bit-retro-styled-pixel-art-illustration-of-a-spooky-green-witch-holding-a-magical-orange-potion",
    "6: L, J. (2019). Trees 8 bit , trees, artist, artwork, digital-art, HD wallpaper. Peakpx. https://www.peakpx.com/en/hd-wallpaper-desktop-kxzab",
    "7: Editors, P. (2020). Black Censor Bar Png - display device, transparent PNG(1280x285) - pngfind. PngFind.com. https://www.pngfind.com/mpng/iJhJxx_black-censor-bar-png-display-device-transparent-png/",
    "8: Clothing, E. (2015). \"Mana pixel potion with stats\" art print for sale by EvolvClothing | Redbubble. RedBubble. https://www.redbubble.com/i/art-print/Mana-Pixel-Potion-with-Stats-by-EvolvClothing/63418989.1G4ZT",
    "9: Birdie, P. (2016). Spooky 16-bit pumpkin by Pixelbirdie on DeviantArt. by PixelBirdie on DeviantArt. https://www.deviantart.com/pixelbirdie/art/Spooky-16-Bit-Pumpkin-642019914",
    "10: Assawarangsitsang, T. (2021). Blue Sky Cloud Bubble Pixel Design for Decoration Wheather Forcast Pixel Design. Vecteezy. https://www.vecteezy.com/png/36395794-blue-sky-cloud-bubble-pixel-design-for-decoration-wheather-forcast-pixel-design"
]

# write citations to a text file
document =  open("citations.txt", "w")
for citation in citations:
    document.write(citation + "\n")
    document.write("\n")

print("Citations have been successfully written into citations.txt!")

document.close() #closes document


class Background:
    def __init__(self):
        self.backdrop = pygame.image.load("backgroundtest.jpg")
        self.backdrop = pygame.transform.scale(self.backdrop, (980, 570))
        
        self.grass = pygame.image.load("grass.png")
        self.grass = pygame.transform.scale(self.grass, (1100, 150))
        self.grass_x1 = 0  
        self.grass_x2 = 980   
        self.grassSpeed = 2
        
        self.dirt = pygame.image.load("bar.png")
        self.dirt = pygame.transform.scale(self.dirt, (1100, 50))

        self.endGame = pygame.image.load("HalloImg.png")
        self.endGame = pygame.transform.scale(self.endGame, (980, 570))

        self.moon = pygame.image.load("moonImage.png")
        self.moon = pygame.transform.scale(self.moon, (200,200))
        
        self.cloud1 = pygame.image.load("cloud2.png")
        self.cloud1 = pygame.transform.scale(self.cloud1, (200, 100))
        self.cloud2 = pygame.image.load("cloud2.png")
        self.cloud2 = pygame.transform.scale(self.cloud2, (200, 100))
        self.cloud3 = pygame.image.load("cloud2.png")
        self.cloud3 = pygame.transform.scale(self.cloud3, (200, 100))
        
        self.cloud1_x = 100
        self.cloud2_x = 500
        self.cloud3_x = 750
        self.cloud1Speed = 1
        self.cloud2Speed = 2
        self.cloud3Speed = 1.5

        # font initialization
        self.font_big = pygame.font.SysFont("constantia", 48)
        self.font_small = pygame.font.SysFont("constantia", 24)
        self.font_medium = pygame.font.SysFont("constantia", 30)

    def draw(self):
        screen.blit(self.backdrop, (0, 0))
        screen.blit(self.moon, (500,100))
        screen.blit(self.cloud1, (self.cloud1_x, 100))
        screen.blit(self.cloud2, (self.cloud2_x, 50))
        screen.blit(self.cloud3, (self.cloud3_x, 150))

    def grass_cycle(self):
        screen.blit(self.dirt, (-30, 535))
        screen.blit(self.grass, (self.grass_x1, 420))
        screen.blit(self.grass, (self.grass_x2, 420))
        self.grass_x1 -= self.grassSpeed
        self.grass_x2 -= self.grassSpeed

        if self.grass_x1 <= -980:
            self.grass_x1 = 980
        if self.grass_x2 <= -980:
            self.grass_x2 = 980

    def cloud_cycle(self):
        self.cloud1_x -= self.cloud1Speed
        self.cloud2_x -= self.cloud2Speed
        self.cloud3_x -= self.cloud3Speed
        
        if self.cloud1_x <= -200:
            self.cloud1_x = 980
        if self.cloud2_x <= -200:
            self.cloud2_x = 980
        if self.cloud3_x <= -200:
            self.cloud3_x = 980

    def update(self):
        self.grass_cycle()
        self.cloud_cycle()

    def draw_intro(self): # initiates intro screen
        screen.blit(self.backdrop, (0, 0))  
        title_text = self.font_big.render("Welcome to Pumpkin Run!", True, (255, 165, 0))  # Orange
        instructions_text = self.font_small.render("Press SPACE to start", True, (255, 165, 0))  # Orange
        guide_text = self.font_small.render("Press W to jump, and SPACE while jumping to double jump!", True, (255,255,255))
        screen.blit(title_text, (230 ,230))
        screen.blit(instructions_text, (400, 320))
        screen.blit(guide_text, (200, 380))
        
    def end_game(self): # intiates end game screen
        screen.blit(self.endGame, (0, 0))
        game_over_text = self.font_big.render("GAME OVER", True, (255, 0, 0))  # Red
        restart_text = self.font_small.render("Press R to Restart", True, (255, 255, 255))  # White
        end_text = self.font_medium.render("Thanks for Playing!", True, (255,165,0))
        screen.blit(game_over_text, (360, 230))
        screen.blit(restart_text, (400, 330))
        screen.blit(end_text, (380, 520))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_image = pygame.image.load("pumpkin_man.png")
        player_image = pygame.transform.scale(player_image, (100,100))
        self.alive = True

        self.image = player_image
        self.rect = self.image.get_rect(midbottom = (75,540)) # set collision rectangle
        self.rect = self.rect.inflate(-50,0) # adjusting the hitbox
        self.health = 5
        self.current_time = 0 # score for the player

        self.vel = 0 # jump velocity
        self.canJump = True
        self.backstep = 4
        self.step = 3
        self.jump_count = 2
        self.canDouble = False


    def player_input(self):
        keys = pygame.key.get_pressed()
        
        # checks if player jumps or moves left and right
        if keys[pygame.K_w]:
            
            if self.canJump:
                self.vel = -18 # height of the jump
                self.canJump = False
                self.canDouble = True
                
        if keys[pygame.K_SPACE]: # double jump with SPACEBAR
            if self.canDouble:
                self.vel = -18
                self.canDouble = False
                
            
        if keys[pygame.K_a]:
            self.rect.x -= self.backstep # allows the player to move left
        elif keys[pygame.K_d]:
            self.rect.x += self.step # allows the player to move rigt

    def apply_gravity(self): # brings player back to the ground
        self.vel += 1 # increases y value of player over every instance
        self.rect.y += self.vel
        
        if self.rect.bottom >= 540: # checks if player lands on the ground
            self.rect.bottom = 540
            self.vel = 0
            self.canJump = True
            self.canDouble = False
            
    def status(self): # checks for sprite interactions and updates player stats
        global gameOver

        collisions = pygame.sprite.spritecollide(self,obstacle_group,dokill=False)

        # display health
        health_font = pygame.font.SysFont('constantia',24)
        health_text = health_font.render(f'Health: {self.health}',True,(255,255,255))
        screen.blit(health_text, (10,30))

        # display score
        self.current_time += .2 # paces score
        score_font = pygame.font.SysFont('constantia',24)
        score_text = score_font.render(f'Score: {self.current_time:,.0f}',True,(255,255,255)) # rounds score using f string
        screen.blit(score_text, (10,10))


        # checks if player collides with objects
        if collisions:
            for obj in collisions: # iterates through the collided objects as "obj"
                if isinstance(obj, Enemy): # checks for collisions in the Enemy class
                    self.health -= 2
                    obj.rect.x = random.randint(1000,2000)
                elif isinstance(obj, Obstacle): # checks for collitions in the obstacle class
                    if obj.type == 'potion': # checks if obstacle type is a potion
                        self.health += 1 # increases health by 1 when colliding with potion
                        self.health = min(self.health, 10) # caps the health to 10
                        obj.rect.y = random.randint(-900, -300) # resets potion position
                    elif obj.type == 'spike': # checks obstacle type for spike
                        self.health -= 1 # decreases health by 1
                        obj.rect.y = random.randint(-900, -300) # resets spike position
                    elif obj.type == 'spike2': # checks obstacle type for spike
                        self.health -= 2 # decreases health by 1
                        obj.rect.y = random.randint(-900, -300) # resets spike position

        # resets player stats and position
        if self.health <= 0: # intiates end game when player health reaches 0
            self.alive = False
            gameOver = True
            self.health = 5
            self.rect.x = 75
            self.current_time = 0 # score = 0
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.status()

        # keeps player within the bounds
        if self.rect.left <= -15:
            self.rect.x = -15
        if self.rect.x >= 900:
            self.rect.x = 900   


class Enemy(pygame.sprite.Sprite):
    def __init__(self,x):
        super().__init__() # currently there is only a witch enemy. More enemies are able to be added just like in the obstacle class
        enemy_image = pygame.image.load("witch.png")
        enemy_image = pygame.transform.scale(enemy_image, (100,100))

        self.image = enemy_image
        self.rect = self.image.get_rect(midbottom = (x,540))
        self.rect = self.rect.inflate(-40,0) # adjusting the hitbox
        self.speed = random.randint(3,5)

    def walk(self):
        self.rect.x -= self.speed
        if self.rect.left <= -100:  # "respawn" the witch
            self.rect.x = random.randint(1100,3500) # reset the position
            self.speed = random.randint(3, 6)
    
    def update(self):
        self.walk()
        collide = pygame.sprite.groupcollide(player, obstacle_group, dokilla=False, dokillb=False)
            
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type,x,speed):
        super().__init__()
        self.type = type
        
        if type == 'spike': # checks for obstacle type
            spike_image = pygame.image.load("spike.png")
            spike_image = pygame.transform.scale(spike_image, (50,50))
            self.image = spike_image # converting spike_image to the reference of self
            self.rect = self.image.get_rect(midbottom = (x,random.randint(-1200,-300)))
            self.rect = self.rect.inflate(-20,0) # changing hitboxes for spike
        elif type == 'spike2':
            spike2_image = pygame.image.load("spike2.png")
            spike2_image = pygame.transform.scale(spike2_image, (50,50))
            self.image = spike2_image # converting spike2_image to the reference of self
            self.rect = self.image.get_rect(midbottom = (x,random.randint(-3000,-800)))
            self.rect = self.rect.inflate(-20,0) # changing hitboxes for spike2
        elif type == 'potion':
            potion_image = pygame.image.load("potion.png")
            potion_image = pygame.transform.scale(potion_image, (100,100))
            self.image = potion_image # converting potion_image to the reference of self
            self.rect = self.image.get_rect(midbottom = (x,random.randint(-3000,-500)))
            self.rect = self.rect.inflate(-50,-15) # changing hitboxes for potion

        # initiate obstacle movement
        self.rect.y = random.randint(-900,-300)
        self.speed_y = speed # speed for each unique Obstacle object
        self.speed_x = speed - 2 # will ensure that the spike is falling at a normal pace

    def fall(self):
        # regenerate the spikes once they pass the ground
        if (self.type == 'spike' or self.type == 'spike2') and self.rect.bottom >= 600:
            if self.type == 'spike':
                self.rect.y = random.randint(-2000, -300)
                self.rect.x = random.randint(-800, 500)
            if self.type == 'spike2':
                self.rect.y = random.randint(-3000, -300)
                self.rect.x = random.randint(-800, 500)
        # potions will remain on the ground
        if self.type == 'potion' and self.rect.bottom >= 540:
            self.rect.bottom = 540
            self.rect.x -= 2.7
            if self.rect.x <= -100:
                self.rect.y = random.randint(-3000, -300)
                self.rect.x = random.randint(-800, 500)

        # continues updating the x and y
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

    def update(self):
        self.fall()
        collide = pygame.sprite.groupcollide(player,obstacle_group,dokilla=False,dokillb=False) # detects specific sprite collision with player
        

            
# pygame setup
pygame.init()
screen = pygame.display.set_mode((980, 570))
clock = pygame.time.Clock()
pygame.display.set_caption("Pumpkin Run")  # naming the window
running = True
intro = True
gameOver = False

# make our classes callable
background = Background()

player = pygame.sprite.GroupSingle() # intiate player for the Player sprite
player.add(Player()) # add Player to a GroupSingle

obstacle_group = pygame.sprite.Group() # initiate obstacle_group for obstacle sprites
for i in range(4): # adding all threats to the player in one sprite group
    falling_spike = Obstacle('spike',random.randint(-400,600),random.randint(2,3))
    falling_spike2 = Obstacle('spike2',random.randint(-400,600),random.randint(2,3))
    falling_potion = Obstacle('potion',random.randint(-500,1000),3)
    obstacle_group.add(falling_spike)
    obstacle_group.add(falling_spike2)
    obstacle_group.add(falling_potion)
    enemy = Enemy(random.randint(1100,3500))
    obstacle_group.add(enemy) 

#### GAME LOOP ####
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
       
        if event.type == pygame.KEYDOWN:
            if intro and event.key == pygame.K_SPACE: # initiate game input
                intro = False
                
            
            if gameOver and event.key == pygame.K_r: # restart input
                gameOver = False
                intro = True
                obstacle_group.empty()
                for i in range(4): # resets all obstacles upon restart
                    falling_spike = Obstacle('spike',random.randint(-400,600),random.randint(2,3))
                    falling_spike2 = Obstacle('spike2',random.randint(-400,600),random.randint(2,3))
                    falling_potion = Obstacle('potion',random.randint(-500,1000),3)
                    obstacle_group.add(falling_spike)
                    obstacle_group.add(falling_spike2)
                    obstacle_group.add(falling_potion)
                    enemy = Enemy(random.randint(1100,3500))
                    obstacle_group.add(enemy) 

    
    if gameOver:
        background.end_game()  
    elif intro:
        background.draw_intro()
        
    else:
        background.draw()
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        background.update()

    pygame.display.flip()  # update the screen
    clock.tick(60)  # limits FPS to 60
    
pygame.quit()

