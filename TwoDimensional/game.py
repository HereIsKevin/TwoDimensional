import PIL
from tkinter import Tk, Canvas


class Game(object):
    def __init__(
        self,
        title,
        geometry=(800, 600),
        location=(10, 10),
        resizable=(True, True),
    ):
        # initialize tkinter window
        self.game = Tk()
        # self.game.overrideredirect(True)  # probably not needed
        self.game.withdraw()
        self.game.title(title)
        self.game.resizable(*resizable)
        self.game.geometry(
            f"""{geometry[0]}x{geometry[1]}{
            "+" + str(location[0]) if location[0] > 0 else location[0]}{
            "+" + str(location[1]) if location[1] > 0 else location[1]}"""
        )

        # initialize canvas to fill window
        self.canvas = Canvas(self.game)
        self.canvas.pack(anchor="center", fill="both", expand=True)

    def resizable(self, value):
        self.game.resizable(*value)

    def title(self, value):
        self.game.title(value)

    def geometry(self, value):
        self.game.geometry(f"{value[0]}x{value[1]}")

    def location(self, value):
        self.game.geometry(
            f"""{"+" + str(value[0]) if value[0] > 0 else value[0]}{
            "+" + str(value[1]) if value[1] > 0 else value[1]}"""
        )

    def play(self):
        self.game.overrideredirect(False)
        self.game.deiconify()

    def terminate(self):
        self.game.destroy()


class Image(object):
    def __init__(self, path):
        self.image = PIL.Image.open(path)

    def resize(self, height, width, antialias=True):
        if antialias:
            self.image = self.image.resize((width, height), PIL.Image.ANTIALIAS)
        else:
            self.image = self.image.resize((width, height))

    def to_tkimage(self):
        return PIL.ImageTk(self.image)
