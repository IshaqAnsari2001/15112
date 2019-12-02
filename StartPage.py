import pygame

pygame.init()
W = 1422
H = 790
win = pygame.display.set_mode((W,H))

pygame.display.set_caption("Oni And The Magical Forest")

# pygame.transform.flip(photo,True,False)
clock = pygame.time.Clock()

characterDictionary = {}
def updateDictionary(characterDictionary):
    ########################################################## EVIL KNIGHT ######################################################################################
    EKWalkRight = [pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_000.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_001.png'),\
                 pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_002.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_003.png'),\
                 pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_004.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_005.png'),\
                 pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_006.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_RUN_000.png')]

    EKWalkLeft = [pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_000.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_001.png'),\
                 pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_002.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_003.png'),\
                 pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_004.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_005.png'),\
                 pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_006.png'), pygame.image.load('Sprites/Knight/Evil Knight/_RUN/_BRUN_000.png')]

    EKDie = [pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_000.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_000.png'), \
             pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_001.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_001.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_002.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_002.png'), \
             pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_003.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_003.png'), \
             pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_004.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_004.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_005.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_005.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_006.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_006.png'),\
             pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_000.png'), pygame.image.load('Sprites/Knight/Evil Knight/_DIE/_DIE_000.png')]

    ###########################################################################################################################################################
    characterDictionary["Evil Knight"] = (EKWalkRight, EKWalkLeft, EKDie)
updateDictionary(characterDictionary)

def mageScreen():

    pygame.display.set_caption("Choose your Character")

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

        clock.tick(27)

        win.blit(bg, (0,0))
        
        win.blit(button1, (150,559))
        win.blit(pic1, (175, 250))
        
        win.blit(button2, (550,559))
        win.blit(pic2, (575,250))
        
        win.blit(button3, (1000,559))
        win.blit(pic3, (1025,250))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 150 and x < 465) and (y > 559 and y < 677):
                    
                    ########################################################## ICE WIZARD ###########################################################################################################
                    IWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_ice/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/run_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_ice/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/run_4.png')]
                    IWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_ice/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/brun_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_ice/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/brun_4.png')]
                    IWIdle = [pygame.image.load('Sprites/Wizard/wizard_ice/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/idle_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_ice/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/idle_4.png')]
                    ############################################################################################################################################################
                    characterDictionary["Ice Wizard"] = (IWWalkRight, IWWalkLeft, IWIdle)

                    ########################################################## ICE BALL ###########################################################################################################
                    IBallLeft = [pygame.image.load('Sprites/Fireball/blue/keyframes/1.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/2.png'),\
                                 pygame.image.load('Sprites/Fireball/blue/keyframes/3.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/4.png'),\
                                 pygame.image.load('Sprites/Fireball/blue/keyframes/5.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/6.png')]
                    IBallRight = [pygame.image.load('Sprites/Fireball/blue/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/2b.png'),\
                             pygame.image.load('Sprites/Fireball/blue/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/4b.png'),\
                             pygame.image.load('Sprites/Fireball/blue/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/6b.png')]
                    ############################################################################################################################################################
                    characterDictionary["Ice Ball"] = (IBallRight, IBallLeft)
                    print(characterDictionary.keys())
                                        
                if (x > 550 and x < 865) and (y > 559 and y < 677):
                    
                    ########################################################## FIRE WIZARD ###########################################################################################################
                    FWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_fire/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/run_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_fire/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/run_4.png')]
                    FWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_fire/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/brun_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_fire/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/brun_4.png')]
                    FWIdle = [pygame.image.load('Sprites/Wizard/wizard_fire/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/idle_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_fire/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/idle_4.png')]
                    ############################################################################################################################################################
                    characterDictionary["Fire Wizard"] = (FWWalkRight, FWWalkLeft, FWIdle)

                    ########################################################## FIRE BALL ###########################################################################################################
                    FBallLeft = [pygame.image.load('Sprites/Fireball/red/keyframes/1.png'), pygame.image.load('Sprites/Fireball/red/keyframes/2.png'),\
                                 pygame.image.load('Sprites/Fireball/red/keyframes/3.png'), pygame.image.load('Sprites/Fireball/red/keyframes/4.png'),\
                                 pygame.image.load('Sprites/Fireball/red/keyframes/5.png'), pygame.image.load('Sprites/Fireball/red/keyframes/6.png')]
                    FBallRight = [pygame.image.load('Sprites/Fireball/red/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/2b.png'),\
                             pygame.image.load('Sprites/Fireball/red/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/4b.png'),\
                             pygame.image.load('Sprites/Fireball/red/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/6b.png')]
                    ############################################################################################################################################################
                    characterDictionary["Fire Ball"] = (FBallRight, FBallLeft)
                    print(characterDictionary.keys())
                    
                if (x > 1000 and x < 1315) and (y > 559 and y < 677):
                    ########################################################## LIGHTNING WIZARD ###########################################################################################################
                    LWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_lightning/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/run_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_lightning/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/run_4.png')]
                    LWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_lightning/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/brun_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_lightning/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/brun_4.png')]
                    LWIdle = [pygame.image.load('Sprites/Wizard/wizard_lightning/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/idle_2.png'),\
                                 pygame.image.load('Sprites/Wizard/wizard_lightning/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/idle_4.png')]
                    ############################################################################################################################################################
                    characterDictionary["Lightning Wizard"] = (LWWalkRight, LWWalkLeft, LWIdle)
                    
                    ########################################################## LIGHTNING BALL ###########################################################################################################
                    LBallLeft = [pygame.image.load('Sprites/Fireball/pink/keyframes/1.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/2.png'),\
                                 pygame.image.load('Sprites/Fireball/pink/keyframes/3.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/4.png'),\
                                 pygame.image.load('Sprites/Fireball/pink/keyframes/5.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/6.png')]
                    LBallRight = [pygame.image.load('Sprites/Fireball/pink/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/2b.png'),\
                             pygame.image.load('Sprites/Fireball/pink/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/4b.png'),\
                             pygame.image.load('Sprites/Fireball/pink/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/6b.png')]
                    ############################################################################################################################################################
                    characterDictionary["Lightning Ball"] = (LBallRight, LBallLeft)
                    print(characterDictionary.keys())
                    
    pygame.quit()


def defenseScreen():

    pygame.display.set_caption("Choose your Defense Character")

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

        clock.tick(27)

        win.blit(bg, (0,0))
        
        win.blit(button1, (250,559))
        win.blit(pic1, (275, 250))
        
        win.blit(button2, (850,559))
        win.blit(pic2, (875,250))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 250 and x < 565) and (y > 559 and y < 677):
                    
                    ########################################################## GODLY KNIGHT ###########################################################################################################
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
                    characterDictionary["Godly Knight"] = (GKWalkRight, GKWalkLeft, GKIdle)

                    ########################################################## GODLY KNIFE ###########################################################################################################
                    GDaggerLeft = [pygame.image.load('Sprites/Daggers/Godly Knife/daggers1.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers2.png'),\
                                 pygame.image.load('Sprites/Daggers/Godly Knife/daggers3.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers4.png')]
                    GDaggerRight = [pygame.image.load('Sprites/Daggers/Godly Knife/daggers1.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers2.png'),\
                             pygame.image.load('Sprites/Daggers/Godly Knife/daggers3.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers4.png')]
                    ############################################################################################################################################################
                    characterDictionary["Godly Knife"] = (GDaggerRight, GDaggerLeft)
                    print(characterDictionary.keys())
                    
                if (x > 850 and x < 1165) and (y > 559 and y < 677):
                    print("Templar was chosen")
             
    pygame.quit()


def playScreen():

    pygame.display.set_caption("Choose your Character")

    bg = pygame.image.load('Essentials/screen.png').convert()

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

        clock.tick(27)

        win.blit(bg, (0,0))
        
        win.blit(button1, (150,559))
        win.blit(pic1, (175, 250))
        
        win.blit(button2, (550,559))
        win.blit(pic2, (575,250))
        
        win.blit(button3, (1000,559))
        win.blit(pic3, (1025,250))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 150 and x < 465) and (y > 559 and y < 677):
                    print("Agility")
                if (x > 550 and x < 865) and (y > 559 and y < 677):
                    defenseScreen()
                if (x > 1000 and x < 1315) and (y > 559 and y < 677):
                    mageScreen()
    pygame.quit()
        
def startScreen():
    

    bg = pygame.image.load('Essentials/bgmain.png').convert()

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

        clock.tick(27)

        win.blit(bg,(0,0))
        win.blit(button1, (330,350))
        win.blit(button2, (330,445))
        win.blit(button3, (330,540))
        win.blit(button4, (330,635))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Program = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (x > 330 and x < 645) and (y > 350 and y < 468):
                    playScreen()
                if (x > 330 and x < 645) and (y > 445 and y < 563):
                    print("Options")
                if (x > 330 and x < 645) and (y > 540 and y < 658):
                    print("Credits")
                if (x > 330 and x < 645) and (y > 635 and y < 753):
                    print("Exit")
        
    pygame.quit()

startScreen()        
