# Invisible-cloak
This is just a fun project made using python

The main reason which attracted me to this project was because of HARRY POTTER.I am a crazy fan of HARRY POTTER movies.If you too are then you too must definitely try this project.Its super FUN!!!

Now let me explain every line of code in detail


<h2>Before running this file first download the given packages</h2>

1.Numpy

2.Opencv_python

3.Time
<br>
<br>
<br>

In this project i have given green as the colour which it detects.If you wish you can change the colour according to your convinience 

Also refer to this link for the values for different colours   


https://pysource.com/2019/02/15/detecting-colors-hsv-color-space-opencv-with-python/

http://colorizer.org/


<h2>The basic idea is given below:</h2>

1.Capture and store the background frame.

2.Detect the green colored cloth using color detection algorithm.

3.Segment out the green colored cloth by generating a mask.

4.Generate the final augmented output to create the magical effect.
<br>
<br>

`import cv2`

`import numpy as np`

`import time`
<br>
<br>

First, we import numpy, cv2 and time, nothing fancy there.
<br>
<br>
`cap = cv2.VideoCapture(0)`
<br>
<br>

This will return video from the  webcam on your computer.
<br>
<br>
`time.sleep(5)`
<br>
<br>
This line gives some time for webcam to setup

`background=0`<br>
`for i in range(35):`<br>
	`ret,background = cap.read()`
<br>  
<br> 
 In this we have captured the background images and stored it in ret. We have used for loop since when we capture one image the image captured is a bit dark compared to when multiple frames are captured. Hence capturing multiple images of static background with a for loop did the trick for me.
<br>  
<br> 
 `background = np.flip(background,axis=1)`
<br>  
<br> 
 Here we are just flipping the image 
<br> 
 `while(cap.isOpened()):`<br>
	`ret, image = cap.read()`
<br>   
 This while loop reads every frame from the webcam, until the camera is open
 `image = np.flip(image,axis=1)`This one flips the image
 
 `hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)`
 <br>
 `lower_green = np.array([25,52,72])`<br>
	`upper_green = np.array([102,255,255])`<br>
	`mask1 = cv2.inRange(hsv,lower_green,upper_green)` 
  <br>
  <br>
 We will convert the RGB (red-blue-green) to HSV(hue-saturation-value) because RGB values are highly sensitive to illumination and also the ranges for RGB also varies drastically for a small difference in shades.
 <br>
 
 The Hue values actually range between 0-360 degrees but in OpenCV to fit into 8bit value the range is from 0-180. Green colour is represented by 25-102.
 <br>
 
 Saturation represents purity of colour. Pure Red, Green and Blue are considered to be true saturated colours. As saturation decreases the effect of the other two colour component increases. Here we set the above value because our cloth is of highly saturated green color.
 <br>
 
 Value corresponds to the brightness of the image. For a given pixel if the value is increased or decreased then values of R,G and B will increase or decrease respectively but their percentage contribution will remain unchanged. The lower value of the range is 72 so that we can detect green colour in the wrinkeles of the cloth as well.
 <br>
 Finally we then assign those values to mask1
 
 If you wish you can change the colour to red or blue or any other colour.For red you have to use two mask and combine them with + operator as red colour have ranges in two ends of colour panel
 <br><br>
 
 ` blurred = cv2.GaussianBlur(hsv, value,0)`<br><br>
 
 Here we use Gaussian filters which have the properties of processing any sharp edges in images and are smoothed while minimizing too much blurring.This helps in minimising errors in detection.<br>
 
 `mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))`<br><br>
 
 This line of code removes small regions of false detection which will avoid random glitches in the final output.
 
 <h2>Here is the actual logic of the project</h2><br><br>
 
` image[np.where(mask1==255)] = background[np.where(mask1==255)]`<br><br>

What we do in this line is quite simple. We access all the pixels which have value of 255 in the final mask (The pixels corresponding to the detected green colour), and we replace the pixel values with the pixel values of respective coordinates in the background frame. That's the trick. 
<br><br>
`cv2.namedWindow('Final',cv2.WINDOW_AUTOSIZE)`<br><br>

This is just for the window size<br><br>

`cv2.imshow('Final',image)`<br><br>

This produces the output image<br><br>

`k = cv2.waitKey(15)
	if k == 32:
		break`<br><br>
  In this line I have give 32 as the value because it is the value for SPACEBAR in ASCII value for ESCAPE it is 27.So to exit the screen we have to press SPACEBAR (in my case)
  to close the program properly.
  
  
  That's it you have finally succeeded in understanding the project.Go on and do the project!!
    
   
 
  



