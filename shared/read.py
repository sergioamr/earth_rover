
import datetime
import sys
import cv2
import numpy as np
import SharedArray as sa
import time

# import pyximport
# pyximport.install()

# import coils
# import util

DEVICE   = 0
WIDTH    = 640
HEIGHT   = 480
DURATION = 20

# Create the OpenCV video capture object.


# cv2.imshow('im', np.random.rand(100, 100, 3))
# Create the output window.
cv2.namedWindow('fish', cv2.WINDOW_NORMAL)

shared = sa.attach("shm://test3")



# Monitor framerates for the given seconds past.
# framerate = coils.RateTicker((1,5,10))

# Run the loop for designated amount of time.
end = datetime.datetime.now() + datetime.timedelta(seconds=DURATION)
while end > datetime.datetime.now():

    time.sleep(0.04)

    cv2.imshow('fish', shared)
    # Allow HighGUI to process event.
    cv2.waitKey(1)

# cv2.destroyAllWindows()
