import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# SW1 -> D0, SW2 -> D1, SW3 -> D2, SW4 -> D3
PINS = (board.D0, board.D1, board.D2, board.D3)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # pin goes LOW when switch is pressed
    pull=True,                 # enable internal pull-ups
)

# Order here matches PINS above: D0, D1, D2, D3
keyboard.keymap = [
    [
        KC.W,                                  # SW1
        KC.A,                             # SW2
        KC.S,              # SW3
        KC.D,                            # SW4
    ]
]

if __name__ == "__main__":
    keyboard.go()
