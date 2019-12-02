###################################################################### ADVENTURE GAME PROJECT ##############################################################################

# Course Project :: 15-112
# Done By :: Ishaq Ansari
# AndrewId :: iansari
# Class: 2023

###################################################################### INITIALISNG VARIABLES ################################################################ 
import pygame
import random

# Initialisinig the dictionary to hold the platforms
floatingPlatforms = {}
pygame.init()

# Initialisng the width and Height of the screen
W = 1422
H = 790

# creating the window in pygame and fixing the screen caption
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("Oni And The Magical Forest")

clock = pygame.time.Clock()

# initalisng a dictionary to hold all the sprites 
characterDictionary = {}

# initialising various sprites into dictionary
########################################################## MONSTERS #########################################################################################
########################################################## EVIL KNIGHT ######################################################################################
#https://craftpix.net/freebies/2d-fantasy-knight-free-sprite-sheets/
EKWalkRight = [pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_000.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_001.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_002.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_003.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_004.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_005.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_006.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_000.png')]

EKWalkLeft = [pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_000.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_001.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_002.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_003.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_004.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_005.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_006.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_000.png')]

###########################################################################################################################################################
# adding Evil Knights to the Dictionary
characterDictionary["Evil Knight"] = (EKWalkRight, EKWalkLeft)
########################################################## CHEIF TROLL ######################################################################################
CTWalkRight = [pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_000.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_001.png'),\
             pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_002.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_003.png'),\
             pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_004.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_005.png'),\
             pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_006.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/WALK_006.png')]

CTWalkLeft = [pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_000.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_001.png'),\
             pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_002.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_003.png'),\
             pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_004.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_005.png'),\
             pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_006.png'), pygame.image.load('Sprites/Trolls/Cheif Troll/WALK/BWALK_006.png')]
###########################################################################################################################################################
# adding Cheif Troll to the Dictionary
characterDictionary["Cheif Troll"] = (CTWalkRight, CTWalkLeft)
########################################################## JUNGLE TROLL ######################################################################################
JTWalkRight = [pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_000.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_001.png'),\
             pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_002.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_003.png'),\
             pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_004.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_005.png'),\
             pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_006.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/WALK_006.png')]

JTWalkLeft = [pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_000.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_001.png'),\
             pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_002.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_003.png'),\
             pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_004.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_005.png'),\
             pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_006.png'), pygame.image.load('Sprites/Trolls/Jungle Troll/WALK/BWALK_006.png')]
###########################################################################################################################################################
# adding Jungle troll to the Dictionary
characterDictionary["Jungle Troll"] = (JTWalkRight, JTWalkLeft)
########################################################## MOUNTAIN TROLL ######################################################################################
MTWalkRight = [pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_000.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_001.png'),\
             pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_002.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_003.png'),\
             pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_004.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_005.png'),\
             pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_006.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/WALK_006.png')]

MTWalkLeft = [pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_000.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_001.png'),\
             pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_002.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_003.png'),\
             pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_004.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_005.png'),\
             pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_006.png'), pygame.image.load('Sprites/Trolls/Mountain Troll/WALK/BWALK_006.png')]
###########################################################################################################################################################
# adding Mountain troll to the Dictionary
characterDictionary["Mountain Troll"] = (MTWalkRight, MTWalkLeft)

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
########################################################## HEROS ################################################################################################
########################################################## GODLY KNIGHT ###########################################################################################################
#https://craftpix.net/freebies/2d-fantasy-knight-free-sprite-sheets/
GKWalkRight = [pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_000.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_001.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_002.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_003.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_004.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_005.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_006.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_RUN_000.png')]

GKWalkLeft = [pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_000.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_001.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_002.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_003.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_004.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_005.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_006.png'), pygame.image.load('Sprites/Knight/Godly Knight/_RUN/_BRUN_000.png')]

GKIdle = [pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_000.png'), pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_001.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_002.png'), pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_003.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_004.png'), pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_005.png'),\
             pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_006.png'), pygame.image.load('Sprites/Knight/Godly Knight/_IDLE/_IDLE_000.png')]

############################################################################################################################################################
# adding Godly Knights to the Dictionary
characterDictionary["Godly Knight"] = (GKWalkRight, GKWalkLeft, GKIdle)
########################################################## TEMPLAR KNIGHT ###########################################################################################################
#https://craftpix.net/freebies/2d-fantasy-knight-free-sprite-sheets/
TKWalkRight = [pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_000.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_001.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_002.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_003.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_004.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_005.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_006.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_RUN_000.png')]

TKWalkLeft = [pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_000.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_001.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_002.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_003.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_004.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_005.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_006.png'), pygame.image.load('Sprites/Knight/Normal Knight/_RUN/_BRUN_000.png')]

TKIdle = [pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_000.png'), pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_001.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_002.png'), pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_003.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_004.png'), pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_005.png'),\
             pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_006.png'), pygame.image.load('Sprites/Knight/Normal Knight/_IDLE/_IDLE_000.png')]

############################################################################################################################################################
# adding Templar Knights to the Dictionary
characterDictionary["Templar Knight"] = (TKWalkRight, TKWalkLeft, TKIdle)
########################################################## Elf Archer ###########################################################################################################
# https://craftpix.net/freebies/2d-fantasy-elf-free-sprite-sheets/
EAWalkRight = [pygame.image.load('Sprites/Archer/2_WALK_000.png'), pygame.image.load('Sprites/Archer/2_WALK_001.png'),\
             pygame.image.load('Sprites/Archer/2_WALK_002.png'), pygame.image.load('Sprites/Archer/2_WALK_003.png'),\
             pygame.image.load('Sprites/Archer/2_WALK_004.png'), pygame.image.load('Sprites/Archer/2_WALK_000.png')]

EAWalkLeft = [pygame.image.load('Sprites/Archer/2_BWALK_000.png'), pygame.image.load('Sprites/Archer/2_BWALK_001.png'),\
             pygame.image.load('Sprites/Archer/2_BWALK_002.png'), pygame.image.load('Sprites/Archer/2_BWALK_003.png'),\
             pygame.image.load('Sprites/Archer/2_BWALK_004.png'), pygame.image.load('Sprites/Archer/2_BWALK_000.png')]

EAIdle = [pygame.image.load('Sprites/Archer/1_IDLE_000.png'), pygame.image.load('Sprites/Archer/1_IDLE_001.png'),\
             pygame.image.load('Sprites/Archer/1_IDLE_002.png'), pygame.image.load('Sprites/Archer/1_IDLE_003.png'),\
             pygame.image.load('Sprites/Archer/1_IDLE_004.png'), pygame.image.load('Sprites/Archer/1_IDLE_000.png')]
############################################################################################################################################################
# adding Elf Archer to the Dictionary
characterDictionary["Elf Archer"] = (EAWalkRight, EAWalkLeft, EAIdle)
########################################################## FIRE WIZARD ###########################################################################################################
#https://craftpix.net/freebies/wizard-character-free-sprite/
FWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_fire/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/run_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_fire/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/run_4.png')]
FWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_fire/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/brun_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_fire/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/brun_4.png')]
FWIdle = [pygame.image.load('Sprites/Wizard/wizard_fire/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/idle_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_fire/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/idle_4.png')]
############################################################################################################################################################
# adding Fire Wizard to the Dictionary
characterDictionary["Fire Wizard"] = (FWWalkRight, FWWalkLeft, FWIdle)
########################################################## ICE WIZARD ###########################################################################################################
#https://craftpix.net/freebies/wizard-character-free-sprite/
IWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_ice/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/run_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_ice/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/run_4.png')]

IWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_ice/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/brun_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_ice/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/brun_4.png')]

IWIdle = [pygame.image.load('Sprites/Wizard/wizard_ice/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/idle_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_ice/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/idle_4.png')]
############################################################################################################################################################
# adding Ice Wizard to the Dictionary
characterDictionary["Ice Wizard"] = (IWWalkRight, IWWalkLeft, IWIdle)
########################################################## LIGHTNING WIZARD ###########################################################################################################
#https://craftpix.net/freebies/wizard-character-free-sprite/
LWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_lightning/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/run_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_lightning/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/run_4.png')]
LWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_lightning/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/brun_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_lightning/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/brun_4.png')]
LWIdle = [pygame.image.load('Sprites/Wizard/wizard_lightning/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/idle_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_lightning/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/idle_4.png')]
############################################################################################################################################################
# adding Lightning Wizard to the Dictionary
characterDictionary["Lightning Wizard"] = (LWWalkRight, LWWalkLeft, LWIdle)

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
########################################################## PROJECTLES ######################################################################################
########################################################## FIRE BALL ###########################################################################################################
#https://www.gamedeveloperstudio.com/graphics/viewgraphic.php?item=1k4p441y0p3p8z9a5n
FBallLeft = [pygame.image.load('Sprites/Fireball/red/keyframes/1.png'), pygame.image.load('Sprites/Fireball/red/keyframes/2.png'),\
             pygame.image.load('Sprites/Fireball/red/keyframes/3.png'), pygame.image.load('Sprites/Fireball/red/keyframes/4.png'),\
             pygame.image.load('Sprites/Fireball/red/keyframes/5.png'), pygame.image.load('Sprites/Fireball/red/keyframes/6.png')]
FBallRight = [pygame.image.load('Sprites/Fireball/red/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/2b.png'),\
         pygame.image.load('Sprites/Fireball/red/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/4b.png'),\
         pygame.image.load('Sprites/Fireball/red/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/6b.png')]
############################################################################################################################################################
characterDictionary["Fire Ball"] = (FBallRight, FBallLeft)

########################################################## ICE BALL ###########################################################################################################
#https://www.gamedeveloperstudio.com/graphics/viewgraphic.php?item=1k4p441y0p3p8z9a5n
IBallLeft = [pygame.image.load('Sprites/Fireball/blue/keyframes/1.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/2.png'),\
             pygame.image.load('Sprites/Fireball/blue/keyframes/3.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/4.png'),\
             pygame.image.load('Sprites/Fireball/blue/keyframes/5.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/6.png')]
IBallRight = [pygame.image.load('Sprites/Fireball/blue/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/2b.png'),\
         pygame.image.load('Sprites/Fireball/blue/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/4b.png'),\
         pygame.image.load('Sprites/Fireball/blue/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/6b.png')]
############################################################################################################################################################
characterDictionary["Ice Ball"] = (IBallRight, IBallLeft)

########################################################## LIGHTNING BALL ###########################################################################################################
#https://www.gamedeveloperstudio.com/graphics/viewgraphic.php?item=1k4p441y0p3p8z9a5n
LBallLeft = [pygame.image.load('Sprites/Fireball/pink/keyframes/1.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/2.png'),\
             pygame.image.load('Sprites/Fireball/pink/keyframes/3.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/4.png'),\
             pygame.image.load('Sprites/Fireball/pink/keyframes/5.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/6.png')]
LBallRight = [pygame.image.load('Sprites/Fireball/pink/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/2b.png'),\
         pygame.image.load('Sprites/Fireball/pink/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/4b.png'),\
         pygame.image.load('Sprites/Fireball/pink/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/6b.png')]
############################################################################################################################################################
characterDictionary["Lightning Ball"] = (LBallRight, LBallLeft)

########################################################## ARROW ###########################################################################################################
arrow = pygame.image.load('arrow3.png').convert()
arrow.set_colorkey((255,255,255))
barrow = pygame.image.load('barrow3.png')
barrow.set_colorkey((255,255,255))
ArrowLeft = [arrow, arrow, arrow, arrow, arrow, arrow]
ArrowRight = [barrow, barrow, barrow, barrow, barrow, barrow]
############################################################################################################################################################
characterDictionary["Arrow"] = (ArrowRight, ArrowLeft)

########################################################## GODLY KNIFE ###########################################################################################################
#https://craftpix.net/freebies/free-game-icons-of-fantasy-daggers-pack-2/
GDaggerLeft = [pygame.image.load('Sprites/Daggers/Godly Knife/daggers1.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers2.png'),\
             pygame.image.load('Sprites/Daggers/Godly Knife/daggers3.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers4.png')]
GDaggerRight = [pygame.image.load('Sprites/Daggers/Godly Knife/daggers1.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers2.png'),\
         pygame.image.load('Sprites/Daggers/Godly Knife/daggers3.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers4.png')]
############################################################################################################################################################
characterDictionary["Godly Knife"] = (GDaggerRight, GDaggerLeft)
######################################################### POTIONS ###########################################################################################################
#https://craftpix.net/freebies/free-game-icons-of-fantasy-potions-pack-1/
health = pygame.image.load("Sprites/Potion/potions (5).png")
death = pygame.image.load("Sprites/Potion/potions (7).png")
characterDictionary["Health Potion"] = health
characterDictionary["Death Potion"] = death
############################################################################################################################################################

# [right, left]
characters = characterDictionary

# creating a class that will make the Main Character and includes all of the features of each Hero
class MC():

    # constructor to initialise all the values which defines the Hero
    def __init__(self,x,y,width,height,floatingPlatforms,characterType):

        # loading the character from the dictionary
        self.characterType = characterType
        self.walkRight = characters[self.characterType][0]
        self.walkLeft = characters[self.characterType][1]
        self.idle = characters[self.characterType][2]

        # setting Hero coordinates, Height, width
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.relativeHeroX = self.x - (self.width // 2)
        self.relativeHeroY = self.y - (self.height // 2)

        # Personalising each characters as per their stats 
        if self.characterType == "Elf Archer":
            # providing the elf archer with high movement speed and jump but low damage
            self.vel = 10
            self.jumpCount = 11.50
            self.health = 10
        elif self.characterType == "Godly Knight" or self.characterType == "Templar Knight":
            # providing the knight with high health but low movement speed and jump height
            self.vel = 7
            self.jumpCount = 11
            self.health = 10
        else:
            # providing the Wizard with high damage but low movement speed and jump height
            self.vel = 8
            self.jumpCount = 11
            self.health = 10

        # initialisng the variables to know which state the HEro is like walking Left or jumping etc. 
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 11
        self.standing = True

        # Varibles to calculate whether the Hero is on the platform or not
        self.onplatform = False
        self.onWhichPlatform = ""
        self.neg = 0
        self.mana = 10

        # Making a HitBox around the Hero
        self.hitbox = (self.x + 17, self.y + 11, 95, 110)
        self.i = 0

    # funtion that controsl the basic movement of the Hero
    def movement(self):

        # checking all the keys that is pressed
        keys = pygame.key.get_pressed()
        # implementing moving left 
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel + 1.5
            self.left = True
            self.right = False
            self.standing = False
            
        # implementing moving right     
        elif keys[pygame.K_RIGHT] and self.x < W - self.width - self.vel:
            
            self.x += self.vel
            self.right = True
            self.left = False
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0
            
        # implementing jumping of the character 
        if not (self.isJump):
            if keys[pygame.K_UP]:
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            # implementing the jump Height of characters as per thier personality
            if self.characterType == "Elf Archer":
                # giving agility type character high jump height
                if self.jumpCount >= -11.50:
                    self.neg = 1
                    if self.jumpCount < 0:
                        self.neg = 0
                    self.y -= ((self.jumpCount ** 2) * 0.5 * self.neg) 
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 11.50

            else:
                # giving other type character moderate jump height
                if self.jumpCount >= -11:
                    self.neg = 1
                    if self.jumpCount < 0:
                        self.neg = 0
                    self.y -= ((self.jumpCount ** 2) * 0.5 * self.neg) 
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 11

    # defining the basic gravity over the game 
    def gravity(self):
        #Inplementing Basic gravity            
        if self.onplatform == False:
            self.y += 9.0

    # drawing the character on the screen        
    def draw(self, win):

        # different characters require different cloack speed so making required classification
        if self.characterType != "Elf Archer":
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if not(self.standing):
                if self.left:
                    # Blitting the image of walking left
                    win.blit(self.walkLeft[self.walkCount//4], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    # Blitting the image of walking right
                    win.blit(self.walkRight[self.walkCount//4], (self.x,self.y))
                    self.walkCount +=1
            else:
                # blitting the idle image of the character
                win.blit(self.idle[self.walkCount//4], (self.x,self.y))
                self.walkCount +=1
                
        # blitting the images of elf archer         
        if self.characterType == "Elf Archer":
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if not(self.standing):
                if self.left:
                    # Blitting the image of walking left
                    win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    # Blitting the image of walking right
                    win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                # Blitting the image of walking right
                win.blit(self.idle[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1

        #Drawing dedictaed player health bar 
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 30, 100, 10))
        pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 30, 100 - round((10.0 * (10 - self.health))), 10))
        self.hitbox = (self.x + 10, self.y + 11, 95, 110)
        #pygame.draw.rect(win, (0,0,255), self.hitbox,2)

    #Checking it the player is on the platform or not
    def platform_check(self,floatingPlatforms):
        p1 = floatingPlatforms["platform 1"]
        if self.x + 90 >= p1.startX and self.x + 30 <= p1.endX:
            self.onplatform = False
            if self.y >= p1.startY - 110 and self.y <= p1.startY - 100:
               
                self.onWhichPlatform = p1.name
                self.onplatform = True
        else:
            self.onplatform = False
            # checking if the player is on platform 2
            p2 = floatingPlatforms["platform 2"]
            if self.x + 90 >= p2.startX and self.x + 30 <= p2.endX:
                if self.y >= p2.startY - 110 and self.y <= p2.startY - 100:
                    self.onWhichPlatform = p2.name
                    self.onplatform = True
            else:
                self.onplatform = False
                # checking if the player is on platform 3
                p3 = floatingPlatforms["platform 3"]
                if self.x + 90 >= p3.startX and self.x + 30<= p3.endX:
                    if self.y >= p3.startY - 110 and self.y <= p3.startY - 100:
                        self.onWhichPlatform = p3.name
                        self.onplatform = True
                else:
                    self.onplatform = False
                    # checking if the player is on platform 4
                    p4 = floatingPlatforms["platform 4"]
                    if self.x + 90 >= p4.startX and self.x + 30 <= p4.endX:
                        if self.y >= p4.startY - 110 and self.y <= p4.startY - 100:
                            self.onplatform = True
                            self.onWhichPlatform = p4.name
                    else:
                        self.onplatform = False
                        # checking if the player is on platform 5
                        p5 = floatingPlatforms["platform 5"]
                        if self.x + 90 >= p5.startX and self.x + 30 <= p5.endX:
                            if self.y >= p5.startY - 110 and self.y <= p5.startY - 100:
                                self.onWhichPlatform = p5.name
                                self.onplatform = True
                        else:
                            # if player is not any platform implementing gravity
                            self.onplatform = False

    
    # defining a function that accounts when the character gets hit by the enemey
    def hit(self):
        # reducing player health as per their personality
        if self.characterType == "Elf Archer":
            self.health -= 2
        elif self.characterType == "Godly Knight" or self.characterType == "Templar Knight":
            self.health -= 1 
        else:
            self.health -= 3
        
        if self.health <= 0:
            self.health = 0
            # ending the game when the character's health drops below zero
            GameOver()
            #pygame.quit()

# creating a class that will make the Main Character and includes all of the features of each enemy            
class Enemy(MC): 
    # constructor to initialise all the values which defines the enemy
    def __init__(self, x, y, width, height, name, floatingPlatforms, heroType, player):

        # loading the character from the dictionary
        self.characterType = heroType
        self.enemyList = ["Evil Knight", "Cheif Troll", "Jungle Troll", "Mountain Troll"]
        self.i = random.randint(0,3)
        self.walkRight = characters[self.enemyList[self.i]][0]
        self.walkLeft = characters[self.enemyList[self.i]][1]
        self.score = 0

        # setting Enemy coordinates, Height, width
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = self.x + 250

        # implementing blitting variables that will be used in the draw function below       
        self.walkCount = 0
        self.vel = 2
        self.jumpCount = 20

        # initialising jump variales required for enemy jumping and staying on the platform
        self.isJump = False
        self.neg = 0
        self.onplatform = False
        self.distance = 0
        self.jumpCount1 = 15
        self.shouldJumpUp = False
        self.shouldJumpDown = False
        self.justJumped = False

        # checking the location of the enemy by storing surrounding platform detalis
        self.onWhichPlatform = ""
        self.platformBefore = ""
        self.platformAfter = ""
        self.jumpkeeper = 0
        self.myPlatformIndex = 0
        self.stop = 1
        

        # initialisng the variables to know which state the enemy is in. 
        self.facing = 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 20
        self.visible = True
        self.platformName = name
        self.deathcount = 0
    
    # definig a function that respawns the enemy after it is killed
    def respawn(self, floatingPlatforms):
        
        p = floatingPlatforms[self.platformName]
        # checking if the platform is out of the screen or not
        if p.isout:
            self.x = p.startX
            self.y = p.startY - self.height
            self.health = 20
            # reinitialising the enemy with different sprites 
            if self.visible == False:
                self.visible = True
                self.i = random.randint(0,2)
                self.walkRight = characters[self.enemyList[self.i]][0]
                self.walkLeft = characters[self.enemyList[self.i]][1]

                # making enemy health full again
                self.health = 20

    # definig a function that respawns the chasing enemy after it is killed
    def heroChaserRespawn(self, floatingPlatforms):
        
        p = floatingPlatforms[self.platformName]
        # checking if the platform is out of the screen or not
        if self.health <= 0:
            self.score += 1
            self.x = p.startX
            self.y = p.startY - self.height - 20
            self.health = 20
            # reinitialising the enemy with different sprites 
            if self.visible == False:
                self.visible = True
                self.i = random.randint(0,2)
                self.walkRight = characters[self.enemyList[self.i]][0]
                self.walkLeft = characters[self.enemyList[self.i]][1]

                # making enemy health full again
                self.health = 20

    # updating the velocity of the enemy in order to keep the enemy on the platform 
    def update(self, floatingPlatforms):
        
        p = floatingPlatforms[self.platformName]
        # making sure that enemy can patrol the moving platform
        if self.x + self.vel + (self.width//1) >= p.endX:
            self.facing = -1
            self.vel = 4.5
            self.vel *= self.facing
            
        
        # making sure that enemy stays on the moving platform
        if self.x + self.vel + (self.width//2) < p.startX:
            self.vel = -2.5
            self.facing = -1
            self.vel *= self.facing

        # keeping the enemy continuously moving at all times
        self.x += self.vel

    # implementing the AI fro the patroling enemy     
    def AI(self, player):
        
        if player.onWhichPlatform == self.platformName:
            displacement = self.x - player.x
            # Changing the direction of the enem in order to move towards the Hero
            if displacement > 0 and self.vel > 0:
                self.vel = 4.5
                self.vel *= -1
            # Changing the direction of the enem in order to move towards the Hero
            if displacement < 0 and self.vel < 0:
                self.vel = -2.5
                self.vel *= -1
                
    # Definig a function that it will chase the Hero
    def heroChase(self, player, floatingPlatforms):

        # making the list of all platforms
        platforms = ["platform 1", "platform 2", "platform 3", "platform 4", "platform 5"]
        
        # creatig enemy platform object
        Myp = floatingPlatforms[self.onWhichPlatform]
        self.myPlatformIndex = platforms.index(self.onWhichPlatform)
        
        # creating the object of the platform before enemy
        self.platformBefore = platforms[self.myPlatformIndex - 1]
        pBefore = floatingPlatforms[self.platformBefore]

        if self.myPlatformIndex != 4:
            self.platformAfter = platforms[self.myPlatformIndex + 1]
            pAfter = floatingPlatforms[self.platformAfter]
        else:
            pAfter = floatingPlatforms["platform 1"]
            
            
        # giving the enemy insteructions on how to jump from platform to platform
        if self.myPlatformIndex < 4:

            # Taking in position of the platform before the current platform and checking if jumping is required
            if self.x + self.width//1.2 <= Myp.startX and Myp.startY < pBefore.startY:
                self.x += self.vel
                
            # Taking in position of the platform before the current platform and checking if jumping is required    
            if self.x + self.width//1.2 <= Myp.startX and Myp.startY > pBefore.startY and self.justJumped == False:
                if self.jumpkeeper == 0:
                    self.jumpup()
                    self.x -= self.vel
                    self.justJumped = True
                    self.jumpkeeper = 1
                    
            # Taking in position of the platform after the current platform and checking if jumping is required        
            if self.x + self.width//1.2 >= Myp.endX and Myp.startY < pAfter.startY:
                self.x += self.vel

            # Taking in position of the platform after the current platform and checking if jumping is required
            if self.x + self.width//1.2 >= Myp.endX and Myp.startY > pAfter.startY and self.justJumped == False:
                if self.jumpkeeper == 0:
                    self.jumpup()
                    self.x += self.vel
                    self.justJumped = True
                    self.jumpkeeper = 1

        else:
            # Taking in position of the platform generated by the current platform and checking if jumping is required
            if self.x + self.width//1.2 <= Myp.startX:
                if self.jumpkeeper == 0:
                    self.jumpup()
                    self.x -= self.vel
                    self.justJumped = True
                    self.jumpkeeper = 1
                    
            # Taking in position of the platform generated by the current platform and checking if jumping is required        
            if self.x + self.width//1.2 >= Myp.endX:
                if self.jumpkeeper == 0:
                    self.jumpup()
                    self.x += self.vel
                    self.justJumped = True
                    self.jumpkeeper = 1 

        # making the enemy move continuosly
        self.x += self.vel

        # calculating the distace between the enemy and Hero 
        self.distance = self.x - player.x

        # changing the facong of the enemy to move towards Hero
        if self.distance > 0 and self.vel > 0:
            self.vel *= -1
            self.vel = -4.5

        # changing the facong of the enemy to move towards Hero    
        if self.distance < 0 and self.vel < 0:
            self.vel = -3.0
            self.vel *= -1
            
        if self.distance == 0:
            self.vel = 0.1
            self.x = player.x

        # setting restriction on when the enemy can jump    
        if self.onplatform == True:
            self.jumpCount = 12
            self.jumpkeeper = 0

        if self.x + self.width//1.2 > Myp.startX + 50 and self.x + self.width//1.2 < Myp.endX - 30:
            self.justJumped = False
        
    # drawing the enemy on the screen    
    def draw(self,win):
        #self.move()
            
        # drawing the enemy if it is visible    
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                if self.i != 0:
                    # Blitting the image of walking right
                    win.blit(self.walkRight[self.walkCount //2], (self.x, self.y))
                    self.walkCount += 1
                else:
                    # Blitting the image of walking right for a specific enemy
                    win.blit(self.walkRight[self.walkCount //4], (self.x, self.y))
                    self.walkCount += 1

            if self.vel < 0:
                if self.i != 0:
                    # Blitting the image of walking left for a specific enemy
                    win.blit(self.walkLeft[self.walkCount //2], (self.x, self.y))
                    self.walkCount += 1
                else:
                    # Blitting the image of walking left
                    win.blit(self.walkLeft[self.walkCount //4], (self.x, self.y))
                    self.walkCount += 1
                    
                
            #Drawing dedictaed health bar for each enemy
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10))
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 100 - round((5.0 * (20 - self.health))), 10))
            self.hitbox = (self.x + 10, self.y , 95, 110)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    # making a function that can make the enemy Jump
    def jumpup(self):
        
        if self.jumpCount1 >= -15:
            self.neg = 1
            if self.jumpCount1 < 0:
                self.neg = -0
            # having a quadratic value updation to make realistic enemy jumping
            self.y -= ((self.jumpCount1 ** 2) * 0.95 * self.neg)
            if self.vel < 0:
                self.x -= ((self.jumpCount1 + 5) **2) * 0.20
                
            if self.vel > 0:
                self.x += ((self.jumpCount1 + 5) **2) * 0.20
                
            self.jumpCount1 -= 1
            
        if self.isJump == False:
            self.jumpCount1 = 15
        
    # making a function to check if the enemy is on platform
    def platform_check(self,floatingPlatforms):
        # checking if the enemy is on platform 1
        p1 = floatingPlatforms["platform 1"]

        if self.x + 105 >= p1.startX and self.x + 70 <= p1.endX:
            self.onplatform = False
            if self.y >= p1.startY - 110 and self.y <= p1.startY - 100:
                self.onWhichPlatform = p1.name
                self.onplatform = True
  
        else:
            self.onplatform = False
            # checking if the enemy is on platform 2
            p2 = floatingPlatforms["platform 2"]
           
            if self.x + 105 >= p2.startX and self.x + 70 <= p2.endX:
                if self.y >= p2.startY - 110 and self.y <= p2.startY - 100:
                    self.onWhichPlatform = p2.name
                    self.onplatform = True     
            else:
                self.onplatform = False
                # checking if the enemy is on platform 3
                p3 = floatingPlatforms["platform 3"]

                if self.x + 105 >= p3.startX and self.x + 70 <= p3.endX:
                    if self.y >= p3.startY - 110 and self.y <= p3.startY - 100:
                        self.onWhichPlatform = p3.name
                        self.onplatform = True
                else:
                    self.onplatform = False
                    # checking if the enemy is on platform 4
                    p4 = floatingPlatforms["platform 4"]
                    if self.x + 105 >= p4.startX and self.x + 70 <= p4.endX:
                        if self.y >= p4.startY - 110 and self.y <= p4.startY - 100:
                            self.onplatform = True
                            self.onWhichPlatform = p4.name
                    else:
                        self.onplatform = False
                        # checking if the enemy is on platform 5
                        p5 = floatingPlatforms["platform 5"]
                        if self.x + 105 >= p5.startX and self.x + 70 <= p5.endX:
                            if self.y >= p5.startY - 110 and self.y <= p5.startY - 100:
                                self.onWhichPlatform = p5.name
                                self.onplatform = True
                        else:
                            # implementing gravity as enemy is not on any platform
                            self.onplatform = False

    # implementing gravity for the enemy
    def gravity(self):
        #Implementing Basic gravity            
        if self.onplatform == False:
            self.y += 10.0
            
    # function that accounts for when the player attacks the enemy
    def hit(self):

        # reducing enemy health when hit by different hero's
        if self.health > 0:
            if self.i == 0:
                if self.characterType == "Elf Archer":
                    self.health -= 6
                elif self.characterType == "Godly Knight" or self.characterType == "Templar Knight":
                    self.health -= 4
                else:
                    self.health -= 8
            else:
                if self.characterType == "Elf Archer":
                    self.health -= 5  
                elif self.characterType == "Godly Knight" or self.characterType == "Templar Knight":
                    self.health -= 4
                else:
                    self.health -= 6
                
        # making the enemy disapper when the health is zero    
        if self.health <= 0:
            self.score += 1
            self.visible = False
            
    
# class that makes all the projectiles that is used by Hero
class projectile(MC):
    
    # initilaisng all the prjectile details needed such as speed and projectile type
    def __init__(self,x,y,radius,color,ballfacing, ballType,Hero):

        # loading the projectile from the dictionary
        self.ballLeft = characters[ballType][1]
        self.ballRight = characters[ballType][0]
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        # checking in which direction is the Hero facing
        self.ballfacing = ballfacing

        # different projectile speed as per Character
        if Hero.characterType == "Elf Archer":
            self.vel = 10 * self.ballfacing
        elif Hero.characterType == "Godly Knight" or Hero.characterType == "Templar Knight":
            self.vel = 7 * self.ballfacing
        else:
            self.vel = 4 * self.ballfacing
        self.moveCount = 0

    # drawing the projectile on the screen
    def draw(self,win):
        
        if self.moveCount + 1 >= 12:
            self.moveCount = 0
        if self.ballfacing == 1:  # facing right
            # Blitting the image of moving right
            win.blit(self.ballRight[self.moveCount//4], (self.x - 25,self.y - 25))
            self.moveCount +=1
        else: # facing left
            # Blitting the image of moving left
            win.blit(self.ballLeft[self.moveCount//4], (self.x - 25,self.y - 25))
            self.moveCount +=1
            
        #pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


# creating a class that makes all the platforms
class platformSet1():

    # initilaising all the variables like coordinates, name of platform and picture
    def __init__(self, startX, startY, win, floatingPlatforms,name,pad,Hero,enemy):

        # initialisng variables
        self.health = characters["Health Potion"]
        self.death = characters["Death Potion"]
        self.name = name
        self.startX = startX
        self.startY = startY
        self.endX = 450 + self.startX
        self.endY = self.startY

        self.tempX = 1100
        self.tempY = self.startY
        self.potionAvailable = True
        self.image = self.health

        # Initilialisng platform velocity and varibles that are used to randomly generate platfroms again
        self.vel = -2
        self.i = 0
        self.j = 0
        self.index = 0
        self.photo = pad
        self.isout = False

    # drawing the platform on the screen and blitting the potions on the platform
    def draw_platform(self,win):
        # blitting the photo of the floating rock
        win.blit(self.photo,(self.startX, self.startY - 15))
        #pygame.draw.rect(win, (255,0,0),(self.startX , self.startY, 450, 15))


    # Updating the platforms on the screen
    def update_platform(self):
        self.startX += self.vel
        self.endX += self.vel
        
    # Definig a function that creates potions on the platforms
    def createPotion(self, win, floatingPlatforms):
        if (self.name == "platform 2" or self.name == "platform 4") and self.potionAvailable:
            p = floatingPlatforms[self.name]
            win.blit(self.image,((p.startX + 450//2), p.startY - 100))
            

    def HeroPick(self, Hero, floatingPlatforms):
        if self.name == "platform 2" or self.name == "platform 4":
            p = floatingPlatforms[self.name]
            if Hero.onWhichPlatform == "platform 2" or Hero.onWhichPlatform == "platform 4":
                if (Hero.x + Hero.vel + (Hero.width//2)) >= (p.startX + 450//2) and self.potionAvailable \
                   and (Hero.health < 10) and Hero.onplatform:
                    if self.image == self.health:
                        self.potionAvailable = False
                        Hero.health = 10
                    if self.image == self.death:
                        self.potionAvailable = False
                        Hero.health -= 2
                        

    def enemyPick(self, enemy, floatingPlatforms):
        if self.name == "platform 2" or self.name == "platform 4":
            p = floatingPlatforms[self.name]
            if enemy.onWhichPlatform == "platform 2" or enemy.onWhichPlatform == "platform 4":
                if (enemy.x >= (p.startX + 450//2)) and self.potionAvailable:
                    self.potionAvailable = True
                    self.image = self.death
                
    # a function that is used to create more platforms in the game
    def create_platform(self,floatingPlatforms):

        # making a possible platform list
        possiblePlatform = [160,278,450,622]
        possibleValues = [-1,1]

        # checking if the start of the platforms leaves the screen
        if (self.startX == -10):
            
            # mapping platfrom1 and platfrom 5
            if self.name == "platform 1":
                p5 = floatingPlatforms["platform 5"]
                if p5.startY != 622:
                    self.index = possiblePlatform.index(p5.startY)
                    # generating random vales between 0 to 1
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
            # mapping platfrom1 and platfrom 2        
            if self.name == "platform 2":
                p1 = floatingPlatforms["platform 1"]
                if p1.startY != 622:
                    self.index = possiblePlatform.index(p1.startY)
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
            # mapping platfrom2 and platfrom 3        
            if self.name == "platform 3":
                p2 = floatingPlatforms["platform 2"]
                if p2.startY != 622:
                    self.index = possiblePlatform.index(p2.startY)
                    # generating random vales between 0 to 1
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
            # mapping platfrom3 and platfrom 4        
            if self.name == "platform 4":
                p3 = floatingPlatforms["platform 3"]
                if p3.startY != 622:
                    self.index = possiblePlatform.index(p3.startY)
                    # generating random vales between 0 to 1
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
            # mapping platfrom4 and platfrom 5        
            if self.name == "platform 5":
                p4 = floatingPlatforms["platform 4"]
                if p4.startY != 622:
                    self.index = possiblePlatform.index(p4.startY)
                    # generating random vales between 0 to 1
                    self.j = random.randint(0,1)
                    self.i = self.index + possibleValues[self.j]
                else:
                    self.i = 2
        # checking if the end of platfrom left the screen    
        if (self.endX <= 0):
            self.isout = True
            
            # repositioning the playfrom as per the random y-value
            self.startX = 2300
            self.startY = possiblePlatform[self.i]
            self.endX = 450 + self.startX
            self.endY = self.startY
            
            # reapearing potion
            if (self.name == "platform 2" or self.name == "platform 4") and self.isout == True:
                self.potionAvailable = True
                
            
        else:
            self.isout = False

# a function that draws every thing on the game window            
def redrawGameWindow(win,Hero,enemy1, enemy, p1, p2, p3, p4, p5,floatingPlatforms):

    pygame.draw.rect(win, (0,0,0), (1275, 12, 140, 50),)

    font =  pygame.font.SysFont("comicsaans", 40)
    text = font.render("Score : " + str(int (enemy.score + enemy1.score)) , True, (255,255,255))

    win.blit(text,(1285,23))

    # drawing all the platforms
    p1.draw_platform(win)
    p2.draw_platform(win)
    p3.draw_platform(win)
    p4.draw_platform(win)
    p5.draw_platform(win)

    p2.createPotion(win,floatingPlatforms)
    p4.createPotion(win,floatingPlatforms)

    # drawing the Hero
    Hero.draw(win)

    # drawing the enemey
    enemy.draw(win)
    enemy1.draw(win)
    

    # drawing the bullets
    start = -1
    for bullet in bullets:
        bullet.draw(win)
    # updating the display to show any changes in the characaters
    pygame.display.update()

# a function that accounts for bullet and enemy collision
def bulletCollision(Hero,enemy,bullets,bulletCount, ballType):

    # getting all the pyagme events
    keys = pygame.key.get_pressed()

    # reinitialisng bulletCount if it meets a condition
    if bulletCount > 0:
        bulletCount += 1
    if bulletCount > 3:
        bulletCount = 0
    # going through each bullet and checking if the bullets hits or not
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                # reducing enemy heatlh if the bullet hits
                enemy.hit()
                # destroying the bullet
                bullets.pop(bullets.index(bullet))
                
        # making the bullet travel        
        if bullet.x < W and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    # checking the facing of the Hero and controlling the no. of bullets    
    if keys[pygame.K_SPACE] and bulletCount == 0:
        if Hero.left:
            ballfacing = -1
        else:
            ballfacing = 1
            
        # bullet count
        if len(bullets) < 1 :
            bullets.append(projectile(round(Hero.x + Hero.width //2), round(Hero.y + Hero.height//2), 6, (255,0,0), ballfacing, ballType,Hero))
        bulletCount = 1       

# creating a class that initialises all the game variables of the class            
class gameVariables():
    def __init__(self):

        # INITIAL CONFIG
        self.Program = True
        #https://craftpix.net/freebies/free-cartoon-forest-game-backgrounds/
        self.bg = pygame.image.load('morning.png').convert()

        #https://craftpix.net/freebies/free-cartoon-forest-game-backgrounds/
        self.bg0 = pygame.image.load('morning.png').convert()

        #https://craftpix.net/freebies/free-cartoon-forest-game-backgrounds/
        self.bg1 = pygame.image.load('evening.png').convert()

        #https://craftpix.net/freebies/free-cartoon-forest-game-backgrounds/
        self.bg2 = pygame.image.load('night.png').convert()

        #https://craftpix.net/freebies/free-jumping-up-game-objects/
        self.pad = pygame.image.load('Pad 1.png').convert()
        self.pad.set_colorkey((0,0,0))
        self.W = 1422
        self.H = 790
        self.loopCount = 0

        # HERO CONFIG:
        self.heroX = 0
        self.heroY = 50 
        self.heroWidth = 95
        self.heroHeight = 110
        self.relativeHeroX = self.heroX - (self.heroWidth // 2)
        self.relativeHeroY = self.heroY - (self.heroHeight) - 5

        # VARIABLE DECLARACTION
        self.bulletCount = 0
        self.bullets = []
        self.count = 0
        self.scrollX = 0
        self.rel_x = 0
        self.i = 0
        self.condition = True
        self.condition1 = True  
        
        
bulletCount = 0
bullets = []
 
condition = True
condition1 = True
condition2 = True        
#mainloop
font = pygame.font.SysFont('comicsans', 40, True)

# initialisng the game variables
game = gameVariables()

count = 0
# main funtion of the game where the whole game runs
def main(game, enemy, enemy1,condition, condition1, condition2, bullets, bulletCount,Hero, ballType):

    # initilaising all the platforms of the game
    p1 = platformSet1(0,160,win,floatingPlatforms,"platform 1", game.pad, Hero, enemy)
    floatingPlatforms["platform 1"] = p1
    p2 = platformSet1(550,450,win,floatingPlatforms,"platform 2", game.pad, Hero, enemy)
    floatingPlatforms["platform 2"] = p2
    p3 = platformSet1(1100,278,win,floatingPlatforms,"platform 3", game.pad, Hero, enemy)
    floatingPlatforms["platform 3"] = p3
    p4 = platformSet1(1650,450,win,floatingPlatforms,"platform 4", game.pad, Hero, enemy)
    floatingPlatforms["platform 4"] = p4
    p5 = platformSet1(2200,622,win,floatingPlatforms,"platform 5", game.pad, Hero, enemy)
    floatingPlatforms["platform 5"] = p5


    
    # implementing background music of the game
    music = pygame.mixer.music.load("Battle-inGame.mp3")
    pygame.mixer.music.play(-1)

    # loop that runs as long as game runs
    while game.Program:
        
        clock.tick(27)
    
        # a loop that exits the game if the cross is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.Program = False

        
        # implementing the background scrolling in the game
        game.rel_x = game.scrollX % game.bg.get_rect().width
        if (game.rel_x >= 0 and game.rel_x <= 5):
            # counting when the background must change
            game.count += 1
            game.loopCount += 1
            
        game.count = game.count % 11
        if((game.count) <= 4):
            # changing the background to morning
            game.bg = game.bg0
        elif((game.count) > 4 and game.count <= 7):
            # changing the background to evening
            game.bg = game.bg1
        elif((game.count) > 7 and game.count <= 10):
            # changing the background to night
            game.bg = game.bg2
        win.blit(game.bg, (game.rel_x - game.bg.get_rect().width, 0))
        if game.rel_x < game.W:
                win.blit(game.bg, (game.rel_x, 0))
        game.scrollX -= 3

        #if game.loopCount >= 11:
            
        # function that has Hero movement
        Hero.movement()

        # implementing gravity and checking if Hero stands on a platform or not       
        Hero.gravity()
        Hero.platform_check(floatingPlatforms)

        # implementing gravity on the enemy and checking if it is on a platform
        enemy.platform_check(floatingPlatforms)
        enemy.gravity()


        # updating the enemy repositioning and respawn
        
        #enemy.respawn(floatingPlatforms)
        enemy.heroChaserRespawn(floatingPlatforms)
        enemy1.respawn(floatingPlatforms)
        
        
        #enemy.update(floatingPlatforms)
        enemy1.update(floatingPlatforms)
        

        enemy.heroChase(Hero, floatingPlatforms)
        #enemy.AI(Hero)
        enemy1.AI(Hero)
        

        # making all the platforms move 
        p1.update_platform()
        p2.update_platform()
        p3.update_platform()
        p4.update_platform()
        p5.update_platform()

        p2.createPotion(win, floatingPlatforms)
        p4.createPotion(win, floatingPlatforms)
       
        p2.HeroPick(Hero, floatingPlatforms)
        p4.HeroPick(Hero, floatingPlatforms)

        p2.enemyPick(enemy, floatingPlatforms)


        # recreating a randomly generated platform when one platfrom leaves the screen
        p1.create_platform(floatingPlatforms)
        p2.create_platform(floatingPlatforms)
        p3.create_platform(floatingPlatforms)
        p4.create_platform(floatingPlatforms)
        p5.create_platform(floatingPlatforms)
        
        # checking between hero and enemy bullet collision
        bulletCollision(Hero,enemy,bullets,bulletCount, ballType)
        bulletCollision(Hero,enemy1,bullets,bulletCount, ballType)
        
        # checking for player and enemy collision
        if enemy1.visible:
            
            if Hero.x + (Hero.width//2) >= enemy1.x and Hero.x + Hero.width <= enemy1.x + enemy1.width:
                if (Hero.y + 18 >= enemy1.y) and Hero.y <= enemy1.y + 20 and condition1:
                    # Hero gets hit if the condition is satisfied
                    Hero.hit()
                    condition1 = False
            # making sure the player gets hit only once            
            elif (Hero.x + Hero.width < enemy1.x or Hero.x + Hero.width > enemy1.x + enemy1.width or Hero.y < enemy1.y ) and condition1 == False:
                condition1 = True
               
        # checking for player and enemy collision        
        if enemy.visible:
            if Hero.x + Hero.width//2 >= enemy.x and Hero.x + Hero.width//2 <= enemy.x + enemy.width:
                if (Hero.y + 18 >= enemy.y) and Hero.y <= enemy.y + 20 and condition:
                    # Hero gets hit if the condition is satisfied
                    Hero.hit()
                    condition = False
                    
            # making sure the player gets hit only once                  
            elif (Hero.x + Hero.width < enemy.x or Hero.x + Hero.width > enemy.x + enemy.width or Hero.y < enemy.y ) and condition == False:
                condition = True
        if (enemy.y + enemy.height >= H) or (enemy.y < -200):
            enemy.health = 0
            
        # GAME OVER IF YOU FALL BELOW THE SCREEN
        if (Hero.y + Hero.height >= H):
            game.Program = False
         
        redrawGameWindow(win, Hero, enemy1, enemy, p1, p2, p3, p4, p5,floatingPlatforms)
    pygame.quit()
    quit()

# defining a function that makes the wizard selection screen 
def mageScreen():

    # Making the caption of your screen
    pygame.display.set_caption("Oni and the Magical Forest")

    back = pygame.image.load('backButton.png').convert()
    back.set_colorkey((0,0,0))

    # loading in the essential pictures and creating buttons
    bg = pygame.image.load('Essentials/screen.png').convert()

    button1 = pygame.image.load('Essentials/Ice.png').convert()
    button1.set_colorkey((0,0,0))
    pic1 = pygame.image.load('Essentials/Cute Mage.jpg').convert()
    
    button2 = pygame.image.load('Essentials/Fire.png').convert()
    button2.set_colorkey((0,0,0))
    pic2 = pygame.image.load('Essentials/Fire Mage.jpg').convert()
    
    button3 = pygame.image.load('Essentials/Storm.png').convert()
    button3.set_colorkey((0,0,0))
    pic3 =  pygame.image.load('Essentials/Storm Mage.jpg').convert()
    
    
    x = 0
    y = 0
    Program = True
    while Program:
        # fixing the clock speed
        clock.tick(27)

        # blitting the background and the buttons in their places
        win.blit(bg, (0,0))
        
        win.blit(button1, (150,559))
        win.blit(pic1, (175, 250))
        
        win.blit(button2, (550,559))
        win.blit(pic2, (575,250))
        
        win.blit(button3, (1000,559))
        win.blit(pic3, (1025,250))

        win.blit(back,(20,20))
        # updtaing the screen to show the recent changes
        pygame.display.update()

        # checking if the User clicked the cross button 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False
            # checking for the mouse button positioning
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 20 and x < 100) and (y > 20 and y < 100):
                    playScreen()
                    
                if (x > 150 and x < 465) and (y > 559 and y < 677):
                    # initialising the HERO and ENEMY and starting the game with the selected character
                    Hero = MC(game.heroX, game.relativeHeroY, game.heroWidth, game.heroHeight,floatingPlatforms, "Ice Wizard")
                    
                    enemy = Enemy(1100, (278 - 100), 110, 95, "platform 3", floatingPlatforms, "Ice Wizard", Hero)
                    enemy1 = Enemy(2200, (622 - 100), 110, 95, "platform 5", floatingPlatforms, "Ice Wizard", Hero)
                    main(game, enemy, enemy1, condition, condition1, condition2, bullets, bulletCount, Hero,"Ice Ball")
                                        
                if (x > 550 and x < 865) and (y > 559 and y < 677):
                    # initialising the HERO and ENEMY and starting the game with the selected character
                    Hero = MC(game.heroX, game.relativeHeroY, game.heroWidth, game.heroHeight,floatingPlatforms, "Fire Wizard")
                    enemy = Enemy(1100, (278 - 100), 110, 95, "platform 3", floatingPlatforms, "Fire Wizard", Hero)
                    enemy1 = Enemy(2200, (622 - 100), 110, 95, "platform 5", floatingPlatforms, "Fire Wizard", Hero)
                    main(game, enemy, enemy1, condition, condition1, condition2, bullets, bulletCount, Hero, "Fire Ball")
                    
                    
                if (x > 1000 and x < 1315) and (y > 559 and y < 677):
                    # initialising the HERO and ENEMY and starting the game with the selected character
                    Hero = MC(game.heroX, game.relativeHeroY, game.heroWidth, game.heroHeight,floatingPlatforms, "Lightning Wizard")
                    enemy = Enemy(1100, (278 - 100), 110, 95, "platform 3", floatingPlatforms, "Lightning Wizard", Hero)
                    enemy1 = Enemy(2200, (622 - 100), 110, 95, "platform 5", floatingPlatforms, "Lightning Wizard", Hero)
                    main(game, enemy, enemy1, condition, condition1, condition2, bullets, bulletCount, Hero, "Lightning Ball")
                   
                    
    pygame.quit()
    quit()

# defining a function that makes the Knight selection screen 
def defenseScreen():

    # Making the caption of your screen
    pygame.display.set_caption("Oni and the Magical Forest")

    back = pygame.image.load('backButton.png').convert()
    back.set_colorkey((0,0,0))

    # loading in the essential pictures and creating buttons
    bg = pygame.image.load('Essentials/screen.png').convert()

    button1 = pygame.image.load('Essentials/Paladin.png').convert()
    button1.set_colorkey((0,0,0))
    pic1 = pygame.image.load('Essentials/Paladin Frame.jpg').convert()
    
    button2 = pygame.image.load('Essentials/Templar.png').convert()
    button2.set_colorkey((0,0,0))
    pic2 = pygame.image.load('Essentials/Templar Frame.jpg').convert()
    
    x = 0
    y = 0
    
    Program = True
    while Program:
        # fixing the clock speed
        clock.tick(27)

        # blitting the background and the buttons in their places
        win.blit(bg, (0,0))
        
        win.blit(button1, (250,559))
        win.blit(pic1, (275, 250))
        
        win.blit(button2, (850,559))
        win.blit(pic2, (875,250))
        win.blit(back,(20,20))
        # updtaing the screen to show the recent changes
        pygame.display.update()

        # checking if the User clicked the cross button 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False
                
            # checking for the mouse button positioning
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 20 and x < 100) and (y > 20 and y < 100):
                    playScreen()
                    
                if (x > 250 and x < 565) and (y > 559 and y < 677):
                    # initialising the HERO and ENEMY and starting the game with the selected character
                    Hero = MC(game.heroX, game.relativeHeroY, game.heroWidth, game.heroHeight,floatingPlatforms, "Godly Knight")
                    enemy = Enemy(1100, (278 - 100), 110, 95, "platform 3", floatingPlatforms, "Godly Knight", Hero)
                    enemy1 = Enemy(2200, (622 - 100), 110, 95, "platform 5", floatingPlatforms, "Godly Knight", Hero)
                    main(game, enemy, enemy1, condition, condition1, condition2, bullets, bulletCount, Hero, "Godly Knife")
                   
                    
                if (x > 850 and x < 1165) and (y > 559 and y < 677):
                    # initialising the HERO and ENEMY and starting the game with the selected character
                    Hero = MC(game.heroX, game.relativeHeroY, game.heroWidth, game.heroHeight,floatingPlatforms, "Templar Knight")
                    enemy = Enemy(1100, (278 - 100), 110, 95, "platform 3", floatingPlatforms, "Templar Knight", Hero)
                    enemy1 = Enemy(2200, (622 - 100), 110, 95, "platform 5", floatingPlatforms, "Templar Knight", Hero)
                    main(game, enemy, enemy1, condition, condition1, condition2, bullets, bulletCount, Hero, "Godly Knife")
                  
             
    pygame.quit()
    quit()

# defining a function that makes the character selection screen 
def playScreen():
    # Making the caption of your screen
    pygame.display.set_caption("Oni and the Magical Forest")

    # loading in the essential pictures and creating buttons
    bg = pygame.image.load('Essentials/screen.png').convert()

    back = pygame.image.load('backButton.png').convert()
    back.set_colorkey((0,0,0))

    button1 = pygame.image.load('Essentials/Agility.png').convert()
    button1.set_colorkey((0,0,0))
    pic1 = pygame.image.load('Essentials/Archer.jpg').convert()
    
    button2 = pygame.image.load('Essentials/Defense.png').convert()
    button2.set_colorkey((0,0,0))
    pic2 = pygame.image.load('Essentials/Paladin Frame.jpg').convert()
    
    button3 = pygame.image.load('Essentials/Mage.png').convert()
    button3.set_colorkey((0,0,0))
    pic3 =  pygame.image.load('Essentials/Cute Mage.jpg').convert()
    
    x = 0
    y = 0
    Program = True
    while Program:
        # fixing the clock speed
        clock.tick(27)
        
        # blitting the background and the buttons in their places
        win.blit(bg, (0,0))
        
        win.blit(button1, (150,559))
        win.blit(pic1, (175, 250))
        
        win.blit(button2, (550,559))
        win.blit(pic2, (575,250))
        
        win.blit(button3, (1000,559))
        win.blit(pic3, (1025,250))

        win.blit(back,(20,20))
        # updtaing the screen to show the recent changes
        pygame.display.update()

        # checking if the User clicked the cross button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False

            # checking for the mouse button positioning
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 20 and x < 100) and (y > 20 and y < 100):
                    startScreen()
                    
                if (x > 150 and x < 465) and (y > 559 and y < 677):
                    # initialising the HERO and ENEMY and starting the game with the selected character
                    Hero = MC(game.heroX, game.relativeHeroY, game.heroWidth, game.heroHeight,floatingPlatforms, "Elf Archer")
                    enemy = Enemy(1300, (278 - 100), 110, 95, "platform 3", floatingPlatforms, "Elf Archer", Hero)
                    enemy1 = Enemy(2200, (622 - 100), 110, 95, "platform 5", floatingPlatforms, "Elf Archer", Hero)
                    main(game, enemy, enemy1, condition, condition1, condition2, bullets, bulletCount, Hero, "Arrow")
                if (x > 550 and x < 865) and (y > 559 and y < 677):
                    # calling in the defense character selection function
                    defenseScreen()
                if (x > 1000 and x < 1315) and (y > 559 and y < 677):
                    # calling in the Mage character selection function
                    mageScreen()
    pygame.quit()
    quit()
    
def GameOver():
    
    gameover = pygame.image.load('Essentials/Gameover.jpg').convert()
    x = 0
    y = 0
    Program = True
    while Program:
        # fixing the clock speed
        clock.tick(27)
        # checking if the User clicked the cross button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if (x > 191 and x < 564) and (y > 500 and y < 590):
                        playScreen()
                    if (x > 831 and x < 1205) and (y > 500 and y < 590):
                        startScreen()
                    

        # updtaing the screen to show the recent changes
        pygame.display.update()

        win.blit(gameover,(0,0))
    pygame.quit()
    quit()

    
def optionScreen():
    
    options = pygame.image.load('Essentials/options.jpg').convert()
    back = pygame.image.load('backButton.png').convert()
    back.set_colorkey((0,0,0))
    x = 0
    y = 0
    Program = True
    while Program:
        # fixing the clock speed
        clock.tick(27)

        win.blit(options,(0,0))
        win.blit(back,(20,20))
        # checking if the User clicked the cross button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False

            # checking for the mouse button positioning
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 20 and x < 100) and (y > 20 and y < 100):
                    startScreen()

        # updtaing the screen to show the recent changes
        pygame.display.update()
      

        
    pygame.quit()
    quit()
    
# function that makes the start screen of the game        
def startScreen():
    # implementing background music of the game
    music = pygame.mixer.music.load("Battle-start.mp3")
    pygame.mixer.music.play(-1)

    # loading in the essential pictures and creating buttons
    bg = pygame.image.load('Essentials/bgmain.png').convert()
    options = pygame.image.load('Essentials/options.jpg').convert()

    button1 = pygame.image.load('Essentials/Play.png').convert()
    button1.set_colorkey((0,0,0))

    button2 = pygame.image.load('Essentials/Options.png').convert()
    button2.set_colorkey((0,0,0))

    button3 = pygame.image.load('Essentials/Credits.png').convert()
    button3.set_colorkey((0,0,0))

    button4 = pygame.image.load('Essentials/Quit.png').convert()
    button4.set_colorkey((0,0,0))

    x = 0
    y = 0
    Program = True
    while Program:
        # fixing the clock speed
        clock.tick(27)
        
        # blitting the background and the buttons in their places
        win.blit(bg,(0,0))
        win.blit(button1, (330,350 + 25))
        win.blit(button2, (330,445 + 25))
        win.blit(button4, (330,540 + 25))
        
        #win.blit(button4, (330,635))
        # updtaing the screen to show the recent changes
        pygame.display.update()

        # checking if the User clicked the cross button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False

            # checking for the mouse button positioning
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 330 and x < 645) and (y > 350 and y < 468):
                    playScreen()
                if (x > 330 and x < 645) and (y > 445 and y < 563):
                    optionScreen()                    
                if (x > 330 and x < 645) and (y > 540 and y < 658):
                    pygame.quit()
                    quit()
                
        
    pygame.quit()
    quit()
    
# calling the start screen function
startScreen()        
