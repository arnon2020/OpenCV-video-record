import cv2
import time
import numpy as np

#set camera
cap = cv2.VideoCapture(1)

#path to output video file
output = 'video.avi'

#set fps
fps = 20

#set codec of output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = None
(h, w) = (None, None)

#size image
width  = 640
height = 480

im_W   = int(width / 2)  # im_width_center
im_H   = int(height / 2) # im_height_center

#green box size
box_W  = 400   # box_width_half
box_H  = 400   # box_height_half
box_W  = int(box_W / 2)
box_H  = int(box_H / 2)

GB_x1  = im_W - box_W
GB_x2  = im_W + box_W
GB_y1  = im_H - box_H
GB_y2  = im_H + box_H
GB_Start = (GB_x1, GB_y1)
GB_Stop  = (GB_x2, GB_y2)

while True:
	_, frame     = cap.read()
	image2       = cv2.rectangle(frame.copy(), GB_Start, GB_Stop, (0, 255, 0), 3)
	roi = frame[GB_y1:GB_y2, GB_x1:GB_x2]
	if writer is None:
		(h, w) = roi.shape[:2]
		writer = cv2.VideoWriter(output, fourcc, fps,(w, h), True)
	
	#roi = cv2.flip(roi,1) #reverse roi
	writer.write(roi)
	cv2.imshow('image2',image2)
	key = cv2.waitKey(1) & 0xff
	if key == ord('q'):
		break

cv2.destroyAllWindows()
writer.release()