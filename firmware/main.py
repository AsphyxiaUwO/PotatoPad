import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.display import Display, SSD1306, TextEntry, ImageEntry

keyboard = KMKKeyboard()

PINS = [board.GP26, board.GP27, board.GP28, board.GP29]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.F1, KC.F2, KC.F3, KC.F4]
]

i2c_bus = busio.I2C(board.GP5, board.GP4)
display_driver = SSD1306(
    i2c=i2c_bus,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='NUM', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='NAV', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='0 1 2', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
    ],
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()