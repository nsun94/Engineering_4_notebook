import time

import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24

lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

disp.begin()


disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)


padding = 2
shape_width = 120
top = 0 # top = padding
bottom = height-padding

x = padding

font = ImageFont.load_default()


draw.rectangle((0,0,width,height), outline=0, fill=0)
disp.image(image)
disp.display()

accel, mag = lsm303.read()
accel_x, accel_y, accel_z = accel
mag_x, mag_y, mag_z = mag


perc = 0

draw.rectangle((x, top, x+shape_width, (height-2)*perc), outline=255, fill=0)

disp.image(image)
disp.display()

while True:
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag

	percx = accel_x/1138
	percy = accel_y/1138

	draw.rectangle((x, height, (x+shape_width)*percy, height-(height-2)*percx), outline=255, fill=255)

	disp.image(image)
	disp.display()

	time.sleep(0.1)

	draw.rectangle((0,0,width,height), outline=0, fill=0)

	disp.image(image)
	disp.display()

	time.sleep(0.0000001)
