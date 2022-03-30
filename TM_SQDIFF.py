import cv2
import numpy as np

locationVid = r"C:\Users\arush\OneDrive\Desktop\ASN4\Vid.mp4"
cap = cv2.VideoCapture(locationVid)
while True:
    # reading each frame
    ret, frame = cap.read()
    if ret:
        # converting both images into grey scale
        imageInGrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(r"C:\Users\arush\OneDrive\Desktop\ASN4\god.png", 0)
        w, h = template.shape[::-1]
        # template matching
        res = cv2.matchTemplate(imageInGrey, template, cv2.TM_SQDIFF)
        threshold = 0.59
        # thresholding values
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            # drawing rectangle
            cv2.rectangle(frame, top_left, bottom_right, 255, 2)
        cv2.imshow('Detected', frame)
        cv2.waitKey(25)
        input("hi")
    else:
        break
cap.release()
cv2.destroyAllWindows()
