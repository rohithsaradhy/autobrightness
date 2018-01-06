#!/usr/bin/python
import cv2
import time
from subprocess import call

camera_port = 0 #is the integrated web cam...
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 1

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

def get_image():
    retval, image = camera.read()
    return image


for i in xrange(ramp_frames):
    temp = get_image()


camera_capture = get_image()

file="text.png"
pixel = camera_capture[479,639]
print pixel
sum =0.0
for i in pixel:
    sum += i

avg =  sum/3

print avg
max =240

if avg > 100:
    brightness = 100 * pow(1.08,-pow((max+43 - pow(avg,1.03)),0.5))
else:
    brightness = 100 * pow(1.11,-pow((max+43 - pow(avg,1.14)),0.61))
print brightness
cv2.imwrite(file,camera_capture)
cmd = str(brightness)
print cmd
call(["light","-S",cmd])

del(camera)
