event_codes = {
    # mouse
    "mouse_left_press": "<Button-1>",
    "mouse_right_press": "<Button-3>",
    "mouse_left_move": "<B1-Motion>",
    "mouse_right_move": "<B3-Motion>",
    "mouse_left_release": "<ButtonRelease-1>",
    "mouse_right_release": "<ButtonRelease-3>",
    "mouse_in": "<Enter>",
    "mouse_out": "<Leave>",
    # keyboard focus
    "focus_in": "<FocusIn>",
    "focus_out": "<FocusOut>",
    # keyboard special chars, rest of chars converted as is
    " ": "<space>",
    "<": "<less>",
    # keyboard special keys
    "enter": "<Return>",
    "cancel": "<Cancel>",
    "backspace": "<BackSpace>",
    "tab": "<Tab>",
    "shift": "<Shift_L>",
    "control": "<Control_L>",
    "alt": "<Alt_L>",
    "pause": "<Pause>",
    "capslock": "<Caps_Lock>",
    "escape": "<Escape>",
    "prior": "<Prior>",
    "next": "<Next>",
    "end": "<End>",
    "home": "<Home>",
    "left": "<Left>",
    "up": "<Up>",
    "right": "<Right>",
    "down": "<Down>",
    "print": "<Print>",
    "insert": "<Insert>",
    "delete": "<Delete>",
    "F1": "<F1>",
    "F2": "<F2>",
    "F3": "<F3>",
    "F4": "<F4>",
    "F5": "<F5>",
    "F6": "<F6>",
    "F7": "<F7>",
    "F8": "<F8>",
    "F9": "<F9>",
    "F10": "<F10>",
    "F11": "<F11>",
    "F12": "<F12>",
    "numlock": "<Num_Lock>",
    "scrolllock": "<Scroll_Lock>",
}

mouse_events = [
    "mouse_left_press",
    "mouse_right_press",
    "mouse_left_move",
    "mouse_right_move",
    "mouse_left_release",
    "mouse_right_release",
    "mouse_in",
    "mouse_out",
]


def translate_event(event_code):
    if len(event_code) == 1 and (event_code != " " or event_code != "<"):
        return event_code
    else:
        return event_codes[event_code]


def mouse_event(function):
    def event_handler(event):
        function(
            {
                "type": "mouse",
                "x": event.x,
                "y": event.y,
                "x_root": event.x_root,
                "y_root": event.y_root,
            }
        )

    return event_handler


def keyboard_event(function):
    def event_handler(event):
        function({"type": "keyboard", "char": tk_event.char})

    return event_handler
