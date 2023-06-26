import os
from inky.auto import auto
# from inky import InkyPHAT -> optional, for the older InkyPHATs
from time import sleep
from picamera import PiCamera
from PIL import Image

inky_display = auto()
# inky_display = InkyPHAT("red") -> optional, for the older InkyPHATs
inky_display.set_border(inky_display.WHITE)

camera = PiCamera()
# camera.color_effects = (128,128) -> optional, changes the camera settings to B&W
camera.resolution = (250, 122)	# 212x104 -> optional, for the older InkyPHATs
camera.start_preview()
sleep(2)
camera.capture('/home/pi/fotka.jpg')

# CONVERSION TO .PNG WITH PALETTE TAKEN FROM A SOURCE FILE
photo = Image.open('/home/pi/fotka.jpg')
im = photo.convert('P')

source = Image.open('/home/pi/palette_source.png') # -> this must be an InkyPHAT-palette image, created manually?
converted = im.quantize(palette=source)
converted.save('/home/pi/fotka.png')
os.remove('/home/pi/fotka.jpg')

sleep(2)
foto = Image.open('/home/pi/fotka.png')
inky_display.set_image(foto)
inky_display.show()
