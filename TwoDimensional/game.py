from tkinter import Tk, Canvas


class Game(object):
    def __init__(
        self,
        name,
        dimensions=[800, 600],
        location=[10, 10],
        resizable=[True, True],
    ):
        # variables are to be synced with Tk window, DO NOT CHANGE DIRECTLY
        self._name = name
        self._dimensions = dimensions
        self._location = location
        self._resizable = resizable

        # initialize tkinter window
        self._window = Tk()
        # self._window.overrideredirect(True)  # probably not needed
        self._window.withdraw()
        self._window.title(self._name)
        self._window.geometry(
            f"""{self._dimensions[0]}x{self._dimensions[1]}{
            "+" + str(self._location[0])
            if self._location[0] > 0 else str(self._location[0])}{
            "+" + str(self._location[1])
            if self._location[1] > 0 else str(self._location[1])}"""
        )
        self._window.resizable(*self._resizable)

        # initialize canvas to fill window
        self._canvas = Canvas(self._window, highlightthickness=0)
        self._canvas.pack(anchor="center", fill="both", expand=True)

        self.update()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        try:
            self._name = str(value)
            self._window.title(self._name)
        except ValueError:
            raise ValueError("name must be a string") from None

        self.update()

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):  # value is width by height
        if value[0] < 0 or value[1] < 0:
            raise ValueError("dimensions cannot be negative")

        try:
            self._dimensions = [int(str(value[0])), int(str(value[1]))]
            self._window.geometry(
                f"{self._dimensions[0]}x{self._dimensions[1]}"
            )
        except ValueError:
            raise ValueError("dimensions must be integers") from None

        self.update()

    @property
    def location(self):
        return self._location

    @location.setter
    def location(
        self, value
    ):  # value is x by y, +x from left, -x from right, +y from top, -y from bottom
        try:
            self._location = [int(str(value[0])), int(str(value[1]))]
            self._window.geometry(
                f"""{
                "+" + str(self._location[0])
                if self._location[0] > 0 else str(self._location[0])
                }{
                "+" + str(self._location[1])
                if self._location[1] > 0 else str(self._location[1])
                }"""
            )
        except ValueError:
            raise ValueError("location must be integers") from None

        self.update()

    @property
    def resizable(self):
        return self._resizable

    @resizable.setter
    def resizable(self, value):
        try:
            self._resizable = [bool(value[0]), bool(value[1])]
            self._window.resizable(*resizable)
        except ValueError:
            raise ValueError("resizable must be booleans") from None

        self.update()

    def update(self):
        self._window.update_idletasks()
        self._window.update()

    def play(self, loop=False):
        # self._window.overrideredirect(False)  # probably not needed
        self._window.deiconify()
        self._canvas.focus_set()
        self.update()

        if loop:
            self._window.mainloop()

    def terminate(self):
        self._window.destroy()

    def on(self, function, event, tag=None):
        if tag is None:
            self._canvas.bind(event, function)
        else:
            self._canvas.tag_bind(tag, event, function)
