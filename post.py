#!/usr/bin/python3

import os
import time
import pynput.mouse as m
import pynput.keyboard as kb

# post to public
# URL = 'www.facebook.com'
# POS1 = (698, 439)
# POS2 = (460, 450)
# POS3 = (580, 450)
# POS4 = (680, 680)


# post to a group
URL = 'https://www.facebook.com/groups/python'
POS1 = (500, 400)
POS2 = (460, 450)
POS3 = (580, 450)
POS4 = (680, 680) 


# Controllers
mouse = m.Controller()
kboard = kb.Controller()

# emulates key press and release for each char in a frase
def write(text):
	global kboard
	for c in text:
		kboard.press(c)
		kboard.release(c)
		time.sleep(0.01)

# open facebook on firefox
os.system(f'firefox {URL}')
time.sleep(8)

# click on "what's on your mind" area
mouse.position = (POS1)
mouse.click(m.Button.left)
time.sleep(4)

# write
write("If you are reading this, it means my Python bot worked!")
time.sleep(4)

# expand themes
mouse.position = (POS2)
mouse.click(m.Button.left)
time.sleep(2)

# select theme 
mouse.position = (POS3)
mouse.click(m.Button.left)
time.sleep(2)

# post
mouse.position = (POS4)
mouse.click(m.Button.left)