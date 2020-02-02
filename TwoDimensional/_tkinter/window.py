from tkinter import Tk
from .event import mouse_events, translate_event, mouse_event, keyboard_event


WINDOW_NAME = "window"
WINDOW_DIMENSIONS = (500, 500)
WINDOW_LOCATION = (50, 50)
WINDOW_RESIZABLE = True
WINDOW_SHOW = True


class Window(object):
    def __init__(self):
        self._window = Tk()
        self._window.title(WINDOW_NAME)
        self._window.geometry(
            f"""{
                WINDOW_DIMENSIONS[0]}x{
                WINDOW_DIMENSIONS[1]}+{
                WINDOW_LOCATION[0]}+{
                WINDOW_LOCATION[1]
            }"""
        )
        self._window.resizable(WINDOW_RESIZABLE, WINDOW_RESIZABLE)

        if WINDOW_SHOW:
            self.show()
        else:
            self.hide()

        self._update()

    def _update(self):
        self._window.update_idletasks()
        self._window.update()

    def name(self, value=None):
        if value is None:
            return self._window.title()
        else:
            self._window.title(value)

        self._update()

    def dimensions(self, value=None):
        if value is None:
            width = []
            height = []

            append_to = width

            for item in self._window.geometry():
                if item == "x":
                    append_to = height
                    continue

                if item.isdigit():
                    append_to.append(item)
                else:
                    break

            return (int("".join(width)), int("".join(height)))
        else:
            self._window.geometry(f"{value[0]}x{value[1]}")

        self._update()

    def location(self, value=None):
        if value is None:
            horizontal = []
            vertical = []

            append_to = horizontal

            for item in self._window.geometry().split("+", maxsplit=1)[1]:
                if item == "+":
                    append_to = vertical
                    continue

                append_to.append(item)

            return (int("".join(horizontal)), int("".join(vertical)))
        else:
            self._window.geometry(f"+{value[0]}+{value[1]}")

        self._update()

    def resizable(self, value=None):
        if value is None:
            return self._window.resizable()[0]
        else:
            self._window.resizable(value, value)

        self._update()

    def show(self):
        self._window.deiconify()
        self._update()

    def hide(self):
        self._window.iconify()
        self._update()

    def state(self):
        if self._window.state() == "iconic":
            return "hidden"
        elif self._window.state() == "normal":
            return "shown"

    def destroy(self):
        self._window.destroy()

    def on(self, **kwargs):
        if "function" in kwargs.keys():
            self._window.bind(
                translate_event(kwargs["event"]),
                mouse_event(kwargs["function"])
                if kwargs["event"] in mouse_events
                else keyboard_event(kwargs["function"]),
            )
        else:

            def event_handler(function):
                self._window.bind(
                    translate_event(kwargs["event"]),
                    mouse_event(function)
                    if kwargs["event"] in mouse_events
                    else keyboard_event(function),
                )

            return event_handler
