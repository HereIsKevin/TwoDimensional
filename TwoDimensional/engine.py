import sys
import __main__ as main
import TwoDimensional.game as g


class Engine(object):
    def __init__(self, games, starting_game=0):
        self.games = games
        self.starting_game = starting_game
        self.proceed = True

    def run(self):
        self.games[self.starting_game].play(self)

        while self.proceed:
            pass

        if hasattr(main, "__file__"):  # prevents termination if in REPL
            sys.exit(0)

    def run_game(self, game):
        self.games[game].play(self)

    def exit(self):
        self.proceed = False
