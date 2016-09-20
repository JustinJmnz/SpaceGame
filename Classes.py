'''
Created on Nov 24, 2014

@author: Justin
'''
import pygame
from random import randint
import math 
class BaseClass(pygame.sprite.Sprite): # Sprites
    allSprites = pygame.sprite.Group() # Will contain all the sprites in one group
    def __init__(self,x,y,width,height,imageString): # Constructor        
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allSprites.add(self) # Add this sprite to allSprites group       
        self.image = pygame.image.load(imageString) # Set the sprite to an image
        self.rect = self.image.get_rect() #Rectangle surrounding sprite
        self.rect.x = x  # Set x coordinate of sprite
        self.rect.y = y # Set y coordinate of sprite
        self.width = width # Set width of sprite
        self.height = height # Set height of sprite
    def destroy(self, ClassName): # Destroy method for each sprite
        ClassName.List.remove(self) # Remove myself from the List
        BaseClass.allSprites.remove(self) # Remove myself from the allSprites list
        del self # Delete myself
class EnemyShip(BaseClass):
    List = pygame.sprite.Group() # Group contains all the ships
    def __init__(self,x,y,width,height,imageString):
        BaseClass.__init__(self, x, y, width, height, imageString)
        EnemyShip.List.add(self)
        self.velx = randint(1,4) # Random velocity for each ship
        self.amplitude = randint(20,140) #  How high the ship will go
        self.period = randint(4,5)/100.0 # The amount of space between each wave. Has to be decimal
        self.health = 100
        self.halfHealth = self.health / 2.0

    def motion(self, SCREENWIDTH, explosion): # Motion of enemyShip
        if self.health == 50:
            self.image = pygame.image.load("Images/enemyShipDamaged.png")
            explosion.play(0) # Play sound once
            self.health = 49
        if self.rect.x + self.width > SCREENWIDTH or self.rect.x < 0: # If im at the end of the window or at beginning
            self.velx = -self.velx # Inverse velocity to turn around
        self.rect.x += self.velx # Velocity of x
        self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) +140 # Sin wave (a * sin(bx + c)* y
    @staticmethod
    def updateAll(SCREENWIDTH,explosion): # Update enemyShip health/movement
        for eShip in EnemyShip.List: # For each eShip in EnenmyShip List
            eShip.motion(SCREENWIDTH, explosion) # Move each ship           
            if eShip.health <= 0: # If any ships health <= 0
                eShip.destroy(EnemyShip) # Destroy the ship
                explosion.play(0) # Play destroy sound              
                return True                                                               # a = how high it goes, b = frequency of period, x = length of sprite, y = point of inflectio     
class EnemyProjectile(BaseClass):
    List = pygame.sprite.Group() # List of all enemy projectiles
    def __init__(self, x, y, width, height, imageString):
        BaseClass.__init__(self, x, y, width, height, imageString)
        EnemyProjectile.List.add(self) # Add projectile to list
        self.vely = 8 # Set velocity of projectile
    @staticmethod
    def movement():
        for projectile in EnemyProjectile.List: # For each projectile in EnemyList
            projectile.rect.y += projectile.vely # Each projectile has the same speed
class Ship(BaseClass): # Ship class inherits sprites
    List = pygame.sprite.Group() # Ship group
    def __init__(self,x,y,width,height,imageString): # Default contructor
        BaseClass.__init__(self, x, y, width, height, imageString) # Call BaseClass, ship has all properties of it
        Ship.List.add(self) # Add ship to sprite group called List
        self.velx = 0 # Velocity x = 0
        self.health = 100
        self.isAlive = True
    def motion(self, width): # Motion of the ship
        if self.health < 100 and self.health > 50:
            self.image = pygame.image.load("Images/playerDamaged.png")
        elif self.health < 50 and self.health > 25:
            self.image = pygame.image.load("Images/playerDamaged2.png")
        elif self.health == 1:
            self.image = pygame.image.load("Images/playerDamaged3.png")
        predicted_location = self.rect.x + self.velx # Predict the location of the ship 
        if predicted_location < 0: # If the predicted location is less an screen width
            self.velx = 0 # Stop moving ship
        elif predicted_location + self.width > width: # If the predicted location is more than the screen width
            self.velx = 0 # Stop moving ship
        
        self.rect.x += self.velx # Velocity of the ship += 3
    def update(self): # Update the health
        if self.health < 0: # If health < 0
            self.destroy(Ship) # Destroy the ship
            self.isAlive = False # It's not alive anymore
class ShipProjectile(pygame.sprite.Sprite): # Projectile for each ship
    List = pygame.sprite.Group() # List of all projectiles from the ship
    normalList = []
    def __init__(self, x, y, width, height, imageString, laser): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageString) # Set the sprite to an image
        self.rect = self.image.get_rect() #Rectangle surrounding sprite
        self.rect.x = x  # Set x coordinate of projectile
        self.rect.y = y # Set y coordinate of projectile
        self.width = width # Set width of projectile
        self.height = height # Set height of projectile
        
        try: # Try and get the last element in list. Is empty first time
            lastElement = ShipProjectile.normalList[-1] # Get last element in list
            difference = abs(self.rect.y - lastElement.rect.y) - 50 # (Finds the difference between starting position and last projectile fired) - 100 more pixels
            if difference < self.height: # If difference of projectile is less than the width, delete the projectile from the list
                return # Don't add it to list of sprites so it doesn't get printed
        except Exception: # This will happen once, when the list is empty. First time you press space
            pass
        ShipProjectile.normalList.append(self)
        ShipProjectile.List.add(self) # Add projectile to list      
        self.vely = None # Set velocity of projectile 
        laser.play() # Play the laser
    
    @staticmethod
    def movement(): # Movement for all projectiles by ship
        for projectile in ShipProjectile.List: # For each projectile in the list
            projectile.rect.y += projectile.vely # Each projectile has same speed
class SpaceRocks(BaseClass):
    List = pygame.sprite.Group()
    def __init__(self,x,y,width,height,imageString):
        BaseClass.__init__(self, x, y, width, height, imageString)
        SpaceRocks.List.add(self)
        self.vely = 3     
        self.health = 100
    def motion(self):
        if self.health  == 50:
            self.image = pygame.image.load("Images/meteorSmall.png")
        self.rect.y += self.vely
    @staticmethod
    def updateAll(explosion):
        for rock in SpaceRocks.List:
            rock.motion()
            if rock.health <= 0:
                rock.destroy(SpaceRocks)
                explosion.play(0)
                return True
           
            
