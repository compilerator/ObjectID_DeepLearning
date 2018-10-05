# This enables us to take a Picture using the RaspberryPi Camera
# Use can use normal JPEGs instead or your webcam captures :P
# Just make sure to save the picture as 'example_01.jpg' (without '') as the code 
# is written for that name but you can change it 
import picamera

print("About to Take A Picture")
with picamera.PiCamera() as cam:
    cam.resolution = (640,480)
    cam.capture('/home/pi/Deep_Learning/object-detection-deep-learning/images/example_01.jpg')
print("Picture Taken")    

