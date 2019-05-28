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

while True:
	_, frame     = cap.read()

	if writer is None:
		(h, w) = frame.shape[:2]
		writer = cv2.VideoWriter(output, fourcc, fps,(w, h), True)
	
	writer.write(frame)
	cv2.imshow('frame',frame)

	key = cv2.waitKey(1) & 0xff
	if key == ord('q'):
		break

cv2.destroyAllWindows()
writer.release()