'''
Created on Nov 25, 2014

@author: Justin
'''
import pygame, Classes, random
import sys
def gameLoop(ship, FPS, total_frames, laser, playerHit, SCREENWIDTH, explosion, backgroundSound):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    keys = pygame.key.get_pressed() # Get the key pressed
    if keys[pygame.K_RIGHT]: # If user presses right key
        ship.image = pygame.image.load("Images/playerRight.png") # Picture of ship moving right
        ship.velx = 15
    elif keys[pygame.K_LEFT]: # If user presses left key
        ship.image = pygame.image.load("Images/playerLeft.png") # Picture of ship moving left
        ship.velx = -15
    else: # If no key is pressed don't move ship 
        ship.image = pygame.image.load("Images/player.png")
        ship.velx = 0
    if keys[pygame.K_SPACE] and ship.isAlive == True:
        projectile = Classes.ShipProjectile((ship.rect.x + (ship.width/2)),(ship.rect.y - ship.height), 9, 33, "Images/laserRed.png", laser)
        projectile.vely = -10
    if ship.isAlive == False:
        return False
#     if keys[pygame.K_UP]:
#         backgroundSound.stop()
#     elif keys[pygame.K_DOWN]:
#         backgroundSound.play(-1);
    spawnShip(FPS,total_frames) # Call spawning method
    spawnRock(SCREENWIDTH)
    enemyShooting(FPS, total_frames) # Call shooting method
    collisions(playerHit, explosion)
    
def enemyShooting(FPS, total_frames):
    shootFreq = random.randint(1,100) # Random number 1-100   
    if shootFreq > 95: # If random number is greater than 95
        for enemy in Classes.EnemyShip.List: # For each enemy in enemyList, shoot them all at once            
            Classes.EnemyProjectile((enemy.rect.x + (enemy.width/2)), (enemy.rect.y + enemy.height),9,33,"Images/laserGreen.png")
def spawnRock(SCREENWIDTH):
    a = random.randint(1,100)
    if a > 98:
        x = random.randint(1,SCREENWIDTH)
        Classes.SpaceRocks(x,-50, 44, 42, "Images/meteorSmall.png")
def spawnShip(FPS, total_frames): # Method for spawning each enemy ship
    fourSeconds = FPS * 2
    if total_frames % fourSeconds == 0: # If the total frames can be divided evenly, then spawn an enemyShip
        r = random.randint(1,2) # 50/50 chance that the bug will spawn from left side or right side
        x = 1 # x = Left end of screen
        if r == 2:
            x = 740-98 # x = Right end of screen
        Classes.EnemyShip(x,130,98,50,"Images/enemyShip.png") # Spawn ship at left or right end of screen
def collisions(playerHit, explosion):
    for enemyShip in Classes.EnemyShip.List: # For each ship in the enemySHip list
        eShip = pygame.sprite.spritecollide(enemyShip, Classes.ShipProjectile.List, True) # Find out if an enemyShip collides with any ShipProjectile, KillIt = True
        if len(eShip) > 0: # If the length of the eShip list > 0
            for hit in eShip: # For each hit in the eShip list
                enemyShip.health -= enemyShip.halfHealth # EnemyShips health - 50
    for ship in Classes.Ship.List: # For each ship in the Ship List
        shipVsProjectile = pygame.sprite.spritecollide(ship, Classes.EnemyProjectile.List, True) # Find out if a Ships collides with any EnemyProjectile, KillIt = True
        shipVsRock = pygame.sprite.spritecollide(ship, Classes.SpaceRocks.List, True)
        if len(shipVsProjectile) > 0:# If the length of the allyShip list > 0
            playerHit.play(0) # Play the hit sound
            for hit in shipVsProjectile: # For each hit in allyShip list
                ship.health -= 33 # Ship health - 33
        if len(shipVsRock) > 0:
            playerHit.play(0)
            for hit in shipVsRock:
                ship.health -= 33
    for rock in Classes.SpaceRocks.List:
        r = pygame.sprite.spritecollide(rock, Classes.ShipProjectile.List, False)
        if len(r) > 0:
            for hit in r:
                rock.health -= 50
                explosion.play(0)
        
        
        
        
    
