import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	print("running")
	time.sleep(2)
	camera.capture('camera_test.jpg')
	print("done")
