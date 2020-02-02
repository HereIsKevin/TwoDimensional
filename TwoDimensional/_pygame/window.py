import pygame

WINDOW_NAME = "window"
WINDOW_DIMENSIONS = (500, 500)
WINDOW_LOCATION = (50, 50)
WINDOW_RESIZABLE = True
WINDOW_SHOW = True


class Window(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(size=WINDOW_DIMENSIONS)

