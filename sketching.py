import cv2
import numpy as np


def sketch(image):
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    canny_edges=cv2.Canny(img_gray_blur,10,70)
    ret,mask=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Add text to the frame
    cv2.putText(frame, "Press 'q' to exit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Input",frame)
    cv2.imshow("Our Live Sketcher",sketch(frame))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()