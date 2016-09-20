'''
Created on Nov 24, 2014

@author: Justin
'''
import pygame
import sys
from Classes import *
from Process import gameLoop
#from __builtin__ import str
import time
def main(stillPlaying):
    pygame.init()
    pygame.mixer.init()
    WIDTH = 740
    HEIGHT = 700
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Space Adventure")
    clock = pygame.time.Clock()
    FPS = 60
    RED = (255,0,0)
    total_frames = 0  # Keeps track of all frames created
    backgroundi = pygame.image.load("Images/background.png")
    backgroundimg = backgroundi.convert_alpha()
    
    ship = Ship((WIDTH/2)-37.5,HEIGHT- 91,75,41,"Images/player.png") # Ship is a new sprite at (x,y) with height, width
    
    explosion = pygame.mixer.Sound("Sound/explosion.ogg")
    laser = pygame.mixer.Sound("Sound/laser.ogg")
    backgroundSound = pygame.mixer.Sound("Sound/backgroundSound.ogg")
    playerHit = pygame.mixer.Sound("Sound/boom8.ogg")
    backgroundSound.play(-1) # Play background music forever
    score = 0
    font = pygame.font.SysFont("Arial Black", 25)
    isAlive = True
    highscore = readHighscore()
    while True:
        scoretxt = font.render("Score: " + str(score), 1, RED)
        highscoretxt = font.render("Highscore: " + str(highscore),1,RED)
        window.blit(backgroundimg,(0,0)) # Load background image at location (0,0)
        window.blit(scoretxt, (0, 0))
        window.blit(highscoretxt, (500,0))
        #PROCESSES       
        isAlive = gameLoop(ship, FPS, total_frames, laser, playerHit, WIDTH, explosion, backgroundSound) # MAIN GAME LOOP               
        if isAlive == False:
            endText = font.render("Start Over? Enter Y/N",1, RED)
            keys = pygame.key.get_pressed()
            window.blit(endText,((HEIGHT/2) - 200, (WIDTH/2) - 200))
            if keys[pygame.K_y]:
                stillPlaying = True
                updateHighscore(score)
                BaseClass.allSprites.empty()
                EnemyProjectile.List.empty()
                EnemyShip.List.empty()
                ShipProjectile.List.empty()
                SpaceRocks.List.empty()
                pygame.quit()
                return stillPlaying
            elif keys[pygame.K_n]:
                stillPlaying = False
                updateHighscore(score)
                return stillPlaying
        #PROCESSES
        #LOGIC
        ship.motion(WIDTH) # Moves User ship
        ship.update()
        if SpaceRocks.updateAll(explosion) == True:
            score += 50
        if EnemyShip.updateAll(WIDTH, explosion) == True:
            score += 100
        ShipProjectile.movement() # Movement of all ship projectiles
        EnemyProjectile.movement()
        total_frames += 1 # Add one to total_frames for spawning enemyShips
        #LOGIC              
        #DRAW
        BaseClass.allSprites.draw(window) # Draw all sprites 
        ShipProjectile.List.draw(window) # Draw all projectiles with restrictions
        pygame.display.flip() # Update window---Write last       
        #DRAW
        clock.tick(FPS)
def readHighscore():
    try:
        file = open("Highscore.txt", "r")
        highscoretxt = file.readline()
        highscore = int(highscoretxt)
        file.close()
        return highscore
    except:
        print ("Couldn't read highscore file")
def updateHighscore(score):
    try:
        file = open("Highscore.txt", "r+")
        prevScoretxt = file.readline()
        prevScore = int(prevScoretxt)
        if score > prevScore:
            file.seek(0)
            s = str(score)
            file.write(s)
        file.close()
    except:
        print ("HighScore file couldn't be opened")
    
if __name__ == '__main__':
    stillPlaying = True
    while(stillPlaying == True):
        stillPlaying = main(stillPlaying)
    pass
