Classes File
============

This Fle contains all the Classes for each image. The classes represent objects. For example, the SpaceRock class represents the space rocks.

Base Class
----------
   
.. py:class:: BaseClass
      
   .. py:method:: __init__(x,y,width,height,imageString)
	 
      Constructor for each Sprite.
 	
      x,y = Starting location on screen.
	
      width,height = Of sprite
	
      imageString = Name of image on disk

   .. py:method:: destroy(className)

      className = Object to delete from memory
      
Enemy Ship
----------

.. py:class:: EnemyShip
      
   .. py:method:: __init__(x,y,width,height,imageString)
	 
      Constructor for the Enemy Ship sprite.
 	
      x,y = Starting location on screen.
	
      width,height = Width and Height of sprite.
	
      imageString = Name of image on disk.

      Has health for each ship.

      Inherits from BaseClass.

   .. py:method:: motion(SCREENWIDTH, explosion)

      This method controls the motion of a enemy ship.
 
   .. py:method:: updateAll(SCREENWIDTH,explosion)

      This method updates the motion of the ship and the health of the enemy ship.

Enemy Projectile
----------------

.. py:class:: EnemyProjectile
 
   .. py:method:: __init__(x,y,width,height,imageString)

      Contructor for the Enemy Projectile sprite.

      x,y = Starting location on screen.

      width,height =  Width and Height of sprite.

      imageString = Name of image on disk.

      Inherits from BaseClass.

   .. py:method:: movement()

      Controls the movement of a projectile.

Ship
----

.. py:class:: Ship

   .. py:method:: __init__(x,y,width,height,imageString)

      Contructor for the Ship sprite.

      x,y = Starting location on screen.

      width,height =  Width and Height of sprite.

      imageString = Name of image on disk.

      Ship has health.

      Inherits from BaseClass.

   .. py:method:: motion(width)

      Controls The movement of the Ship.

   .. py:method:: update()

      Update the health of the Ship.

Ship Projectile
---------------

.. py:class:: ShipProjectile

   .. py:method:: __init__(x,y,width,height,imageString)

      Contructor for the Ship Projectile sprite.

      x,y = Starting location on screen.

      width,height =  Width and Height of sprite.

      imageString = Name of image on disk.

      Inherits from BaseClass.

   .. py:method:: movement()

      Controls the movement of a Ship projectile.
     
Space Rocks
-----------

.. py:class:: SpaceRocks
   
   .. py:method:: __init__(x,y,width,height,imageString)

      Contructor for the Space rocks sprite.

      x,y = Starting location on screen.

      width,height =  Width and Height of sprite.

      imageString = Name of image on disk.

      Inherits from BaseClass.

   .. py:method:: motion()

      Controls the motion of each space rock object.

   .. py:method:: updateAll()

      Calls motion method and updates the health.