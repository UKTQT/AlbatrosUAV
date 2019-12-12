import cv2 as cv
import Resolution
import Rectangle
capture = cv.VideoCapture(0)
Resolution.setResolution("PAL")
while True:
    ret, frame = capture.read()
    Rectangle.createRectagle(frame)
    cv.imshow("CAPTURE", frame)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()