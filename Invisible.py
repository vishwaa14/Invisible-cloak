import cv2
import numpy as np
import time

print("""
        PREPARE TO GET INVISIBLE!!!....
    """)


cap = cv2.VideoCapture(0)
time.sleep(5)
background=0
for i in range(35):
	ret,background = cap.read()

background = np.flip(background,axis=1)

while(cap.isOpened()):
	ret, image = cap.read()
	
	# Flipping the image (Can be uncommented if needed)
	image = np.flip(image,axis=1)
	
	# Converting image to HSV color space.
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	value = (35, 35)
	
	blurred = cv2.GaussianBlur(hsv, value,0)
	
	# Defining lower range for green color detection.
	lower_green = np.array([25,52,72])
	upper_green = np.array([102,255,255])
	mask1 = cv2.inRange(hsv,lower_green,upper_green)
	
	
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	
	# Replacing pixels corresponding to cloak with the background pixels.
	image[np.where(mask1==255)] = background[np.where(mask1==255)]
	cv2.namedWindow('Final',cv2.WINDOW_AUTOSIZE)
	cv2.imshow('Final',image)
	k = cv2.waitKey(15)
	if k == 32:
		break
                

	

