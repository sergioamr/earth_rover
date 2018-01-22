
import datetime
import sys
import cv2
import numpy as np
import SharedArray as sa

# import pyximport
# pyximport.install()

# import coils
# import util

DEVICE   = 0
WIDTH    = 640
HEIGHT   = 480
DURATION = 20

# Create the OpenCV video capture object.
cap = cv2.VideoCapture(DEVICE)
print "cap: " , cap
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

# cv2.imshow('im', np.random.rand(100, 100, 3))
# Create the output window.
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

shared = None


# Maintain accumulation of thresholded differences.
image_acc = None

# Keep track of previous iteration's timestamp.
tstamp_prev = None

# Monitor framerates for the given seconds past.
# framerate = coils.RateTicker((1,5,10))

# Run the loop for designated amount of time.
end = datetime.datetime.now() + datetime.timedelta(seconds=DURATION)
while end > datetime.datetime.now():

    # Take a snapshot and mark the snapshot time.
    hello, image = cap.read()
    print "shape", np.shape(image)
    print hello

    if np.shape(image) == (480, 640, 3):

        if shared is None:
            shared = sa.create("shm://test3", np.shape(image), image.dtype)
            b = sa.attach("shm://test3")
        shared[:] = image.copy()

    cv2.imshow('image', image)
    # Allow HighGUI to process event.
    cv2.waitKey(1)

sa.delete("shm://test3")
# cv2.destroyAllWindows()
