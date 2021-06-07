import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)# sets the camera's resolution
	camera.start_preview()# prepares the camera
	# Camera warm-up time
	print("running")
	time.sleep(2)
	camera.capture('camera_test.jpg')# takes a picture and saves it as the file name provided
	print("done")
