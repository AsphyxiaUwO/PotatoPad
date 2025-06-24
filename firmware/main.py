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

bus = busio.I2C(board.GP_SCL, board.GP_SDA);
driver = SSD1306(i2c=bus, device_address=0x3C);
display = Display(
    display=driver,
    width=128,
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
);
display.entries = [
        TextEntry(text='PotatoPad', x=0, y=0, x_anchor="M"),
];

if __name__ == '__main__':
    keyboard.go()
