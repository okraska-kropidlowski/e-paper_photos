import os
from inky.auto import auto
from time import sleep
from picamera import PiCamera
from PIL import Image

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

camera = PiCamera()
camera.color_effects = (128,128) # -> optional, changes the camera settings to B&W
camera.resolution = (212, 104) 
camera.start_preview()
sleep(1)
camera.capture('/home/pi/photo.jpg')

photo = Image.open('/home/pi/photo.jpg')
im = photo.convert('1')
im.save('/home/pi/photo.png')
os.remove('/home/pi/photo.jpg')

foto = Image.open('/home/pi/photo.png')
inky_display.set_image(foto)
inky_display.show()
os.remove('/home/pi/photo.png')
