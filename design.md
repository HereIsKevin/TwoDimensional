# The Structure of TwoDimensional

- *class* Engine
    This is the main object, only one that can exist at any time. It powers the entire game, coordinating all the displayed windows.
    - *def* run
        This begins running the main loop, beginning the process of execution
- *class* Game
    This object represents a game, each of which creates a windows to draw on. Many of these can exist, one for each level.
    - *def* \_\_init\_\_
        Initialize by creating a hidden Tk window, which has many options
    - *def* resizable
        Set which directions is the window resizable
    - *def* title
        Set the title of game window
    - *def* geometry
        Set the geometry (dimensions) of the window
    - *def* location
        Set the location of the window on the screen
    - *def* play
        Show the window, and the inherited play begins to run
    - *def* terminate
        Destroy the window, and execute the inherited cleanup procedure
- *class* Sprite
    This object represents a sprite, which is all other spirtes inherit from
- *class* Image(Sprite)
    This object represents a image to be drawn on the canvas
    - *def* \_\_init\_\_
        Initialize the sprite with its parent game, the image, and optional dimensions
    - *def* draw
        Draw the sprite on the canvas at a specified location
    - *def* move
        Move the sprite in the specified direction n pixels
    - *def* place
        Place the sprite in the specified coordinates
    - *def* bind
        Create a binding of the sprite to a event
