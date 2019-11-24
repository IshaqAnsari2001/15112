import pygame

characterDictionary = {}

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''

########################################################## MONSTERS #########################################################################################
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
########################################################## KNIFE ORK ###########################################################################################################
KOWalkRight = [pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_000.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_001.png'),\
             pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_002.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_003.png'),\
             pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_004.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_005.png'),\
             pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_006.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_000.png')]
KOWalkLeft = [pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_000.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_001.png'),\
             pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_002.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_003.png'),\
             pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_004.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_005.png'),\
             pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_006.png'), pygame.image.load('Sprites/Orcs/Knife Ork/RUN/RUN_000.png')]
############################################################################################################################################################
characterDictionary["Knife Ork"] = (KOWalkRight, KOWalkLeft)
########################################################## HAMMER ORK ###########################################################################################################
HOWalkRight = [pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_000.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_001.png'),\
             pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_002.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_003.png'),\
             pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_004.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_005.png'),\
             pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_006.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_000.png')]
HOWalkLeft = [pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_000.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_001.png'),\
             pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_002.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_003.png'),\
             pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_004.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_005.png'),\
             pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_006.png'), pygame.image.load('Sprites/Orcs/Hammer Ork/RUN/RUN_000.png')]
############################################################################################################################################################
characterDictionary["Hammer Ork"] = (HOWalkRight, HOWalkLeft)
########################################################## AXE ORK ###########################################################################################################
AOWalkRight = [pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_000.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_001.png'),\
             pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_002.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_003.png'),\
             pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_004.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_005.png'),\
             pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_006.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_000.png')]
AOWalkLeft = [pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_000.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_001.png'),\
             pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_002.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_003.png'),\
             pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_004.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_005.png'),\
             pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_006.png'), pygame.image.load('Sprites/Orcs/Axe Ork/RUN/RUN_000.png')]
############################################################################################################################################################
characterDictionary["Axe Ork"] = (AOWalkRight, AOWalkLeft)

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''

########################################################## HEROS ################################################################################################
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
########################################################## FIRE WIZARD ###########################################################################################################
FWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_fire/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/run_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_fire/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/run_4.png')]
FWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_fire/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/brun_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_fire/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/brun_4.png')]
FWIdle = [pygame.image.load('Sprites/Wizard/wizard_fire/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_fire/idle_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_fire/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_fire/idle_4.png')]
############################################################################################################################################################
characterDictionary["Fire Wizard"] = (FWWalkRight, FWWalkLeft, FWIdle)
########################################################## ICE WIZARD ###########################################################################################################
IWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_ice/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/run_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_ice/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/run_4.png')]
IWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_ice/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/brun_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_ice/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/brun_4.png')]
IWIdle = [pygame.image.load('Sprites/Wizard/wizard_ice/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_ice/idle_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_ice/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_ice/idle_4.png')]
############################################################################################################################################################
characterDictionary["Ice Wizard"] = (IWWalkRight, IWWalkLeft, IWIdle)
########################################################## LIGHTNING WIZARD ###########################################################################################################
LWWalkRight = [pygame.image.load('Sprites/Wizard/wizard_lightning/run_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/run_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_lightning/run_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/run_4.png')]
LWWalkLeft = [pygame.image.load('Sprites/Wizard/wizard_lightning/brun_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/brun_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_lightning/brun_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/brun_4.png')]
LWIdle = [pygame.image.load('Sprites/Wizard/wizard_lightning/idle_1.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/idle_2.png'),\
             pygame.image.load('Sprites/Wizard/wizard_lightning/idle_3.png'), pygame.image.load('Sprites/Wizard/wizard_lightning/idle_4.png')]
############################################################################################################################################################
characterDictionary["Lightning Wizard"] = (LWWalkRight, LWWalkLeft, LWIdle)

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''

########################################################## PROJECTLES ######################################################################################
########################################################## FIRE BALL ###########################################################################################################
FBallLeft = [pygame.image.load('Sprites/Fireball/red/keyframes/1.png'), pygame.image.load('Sprites/Fireball/red/keyframes/2.png'),\
             pygame.image.load('Sprites/Fireball/red/keyframes/3.png'), pygame.image.load('Sprites/Fireball/red/keyframes/4.png'),\
             pygame.image.load('Sprites/Fireball/red/keyframes/5.png'), pygame.image.load('Sprites/Fireball/red/keyframes/6.png')]
FBallRight = [pygame.image.load('Sprites/Fireball/red/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/2b.png'),\
         pygame.image.load('Sprites/Fireball/red/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/4b.png'),\
         pygame.image.load('Sprites/Fireball/red/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/red/keyframes/6b.png')]
############################################################################################################################################################
characterDictionary["Fire Ball"] = (FBallRight, FBallLeft)
########################################################## ICE BALL ###########################################################################################################
IBallLeft = [pygame.image.load('Sprites/Fireball/blue/keyframes/1.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/2.png'),\
             pygame.image.load('Sprites/Fireball/blue/keyframes/3.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/4.png'),\
             pygame.image.load('Sprites/Fireball/blue/keyframes/5.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/6.png')]
IBallRight = [pygame.image.load('Sprites/Fireball/blue/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/2b.png'),\
         pygame.image.load('Sprites/Fireball/blue/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/4b.png'),\
         pygame.image.load('Sprites/Fireball/blue/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/blue/keyframes/6b.png')]
############################################################################################################################################################
characterDictionary["Ice Ball"] = (IBallRight, IBallLeft)
########################################################## LIGHTNING BALL ###########################################################################################################
LBallLeft = [pygame.image.load('Sprites/Fireball/pink/keyframes/1.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/2.png'),\
             pygame.image.load('Sprites/Fireball/pink/keyframes/3.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/4.png'),\
             pygame.image.load('Sprites/Fireball/pink/keyframes/5.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/6.png')]
LBallRight = [pygame.image.load('Sprites/Fireball/pink/keyframes/1b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/2b.png'),\
         pygame.image.load('Sprites/Fireball/pink/keyframes/3b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/4b.png'),\
         pygame.image.load('Sprites/Fireball/pink/keyframes/5b.png'), pygame.image.load('Sprites/Fireball/pink/keyframes/6b.png')]
############################################################################################################################################################
characterDictionary["Lightning Ball"] = (LBallRight, LBallLeft)
########################################################## GODLY KNIFE ###########################################################################################################
GDaggerLeft = [pygame.image.load('Sprites/Daggers/Godly Knife/daggers1.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers2.png'),\
             pygame.image.load('Sprites/Daggers/Godly Knife/daggers3.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers4.png')]
GDaggerRight = [pygame.image.load('Sprites/Daggers/Godly Knife/daggers1.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers2.png'),\
         pygame.image.load('Sprites/Daggers/Godly Knife/daggers3.png'), pygame.image.load('Sprites/Daggers/Godly Knife/daggers4.png')]
############################################################################################################################################################
characterDictionary["Godly Knife"] = (GDaggerRight, GDaggerLeft)

def dictionary():
    return(characterDictionary)





