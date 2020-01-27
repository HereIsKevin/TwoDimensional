from TwoDimensional.game import *
from TwoDimensional.sprites import *

game = Game("Test Game")
ball = Image(game, "./ball.png", dimensions=(50, 50))
move_by = 3
ball.draw()

move_up = False
move_down = False
move_left = False
move_right = False

def move(direction, start):
    exec(f"global {direction}; {direction} = {start}")

game.on(event="<Up>")(lambda *x: move("move_up", True))
game.on(event="<Down>")(lambda *x: move("move_down", True))
game.on(event="<Left>")(lambda *x: move("move_left", True))
game.on(event="<Right>")(lambda *x: move("move_right", True))
game.on(event="<KeyRelease-Up>")(lambda *x: move("move_up", False))
game.on(event="<KeyRelease-Down>")(lambda *x: move("move_down", False))
game.on(event="<KeyRelease-Left>")(lambda *x: move("move_left", False))
game.on(event="<KeyRelease-Right>")(lambda *x: move("move_right", False))

game.play()

while True:
    game.update()

    position = ball.position()

    if move_up and position[1] >= 0:
        ball.move_by([0, -move_by])
    if move_down and position[1] <= 600:
        ball.move_by([0, move_by])
    if move_left and position[0] >= 0:
        ball.move_by([-move_by, 0])
    if move_right and position[0] <= 800:
        ball.move_by([move_by, 0])
