import digitalio
import board
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define the keyboard object kbd
kbd = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#define the keypad buttons button
play_pause_button = digitalio.DigitalInOut(board.GP10)
play_pause_button.direction = digitalio.Direction.INPUT
play_pause_button.pull = digitalio.Pull.DOWN

rip_del_button = digitalio.DigitalInOut(board.GP9)
rip_del_button.direction = digitalio.Direction.INPUT
rip_del_button.pull = digitalio.Pull.DOWN

append_button = digitalio.DigitalInOut(board.GP8)
append_button.direction = digitalio.Direction.INPUT
append_button.pull = digitalio.Pull.DOWN

insert_button = digitalio.DigitalInOut(board.GP7)
insert_button.direction = digitalio.Direction.INPUT
insert_button.pull = digitalio.Pull.DOWN

del_button = digitalio.DigitalInOut(board.GP5)
del_button.direction = digitalio.Direction.INPUT
del_button.pull = digitalio.Pull.DOWN

source_button = digitalio.DigitalInOut(board.GP4)
source_button.direction = digitalio.Direction.INPUT
source_button.pull = digitalio.Pull.DOWN

split_button = digitalio.DigitalInOut(board.GP3)
split_button.direction = digitalio.Direction.INPUT
split_button.pull = digitalio.Pull.DOWN

mark_in_button = digitalio.DigitalInOut(board.GP1)
mark_in_button.direction = digitalio.Direction.INPUT
mark_in_button.pull = digitalio.Pull.DOWN

mark_out_button = digitalio.DigitalInOut(board.GP0)
mark_out_button.direction = digitalio.Direction.INPUT
mark_out_button.pull = digitalio.Pull.DOWN

#Main Loop
keep_going = True
key_pressed = False

while keep_going:
    #set led to off if to tell if no button is pressed
    led.value = False

    if mark_in_button.value == True:
        led.value = True
        if not key_pressed: kbd.send(Keycode.I)
        key_pressed = True
    if mark_out_button.value == True:
        led.value = True
        if not key_pressed: kbd.send(Keycode.O)
        key_pressed = True
    if play_pause_button.value == True:
        led.value = True
        if not key_pressed: kbd.send(Keycode.SPACE)
        key_pressed = True
    if rip_del_button.value == True:
        led.value = True
        if not key_pressed: kbd.send(Keycode.CONTROL, Keycode.BACKSPACE)
        key_pressed = True
    if del_button.value == True:
        led.value = True
        if not key_pressed: kbd.send(Keycode.DELETE)
        key_pressed = True
    #if append_button.value == True:
    #    led.value = True
    #    if not key_pressed: kbd.send(Keycode.A)
    #    key_pressed = True
    if insert_button.value == True:
        led.value = True
        if not key_pressed: kbd.send(Keycode.COMMA)
        key_pressed = True
    if split_button.value == True:
        led.value = True
        if not key_pressed: kbd.send(Keycode.CONTROL, Keycode.K)
        key_pressed = True
    #if source_button.value == True:
    #    led.value = True
    #    if not key_pressed: kbd.send(Keycode.T)
    #    key_pressed = True

    if not led.value: key_pressed = False