# The Structure of TwoDimensional

- *class* Engine
    This is the main object, only one that can exist at any time. It powers the entire game, coordinating all the displayed windows.
    - *def* run
        This begins running the main loop, beginning the process of execution
- *class* Game
    This object represents a game, each of which creates a windows to draw on. Many of these can exist, one for each level.
- *class* Sprite
    This object represents a sprite, which is drawn on the display
