import cv2 as cv
import Rectangle
import Resolution
capture = cv.VideoCapture(0)
width = 640
height = 480
#Resolution.setResolution("PAL")
capture.set(cv.CAP_PROP_FRAME_HEIGHT,height)
capture.set(cv.CAP_PROP_FRAME_WIDTH,width)
while True:
    ret, frame = capture.read()
    #Rectangle.createRectagle(frame)
    TARGET_LOCKING_AREA_STOP_POINT = int(((width / 100) * 25)), int(((height / 100) * 10))
    TARGET_LOCKING_AREA_START_POINT = int(((width / 100) * 75)), int(((height / 100) * 90))
    TARGET_LOCKING_AREA_COLOR = (0, 0, 255)
    cv.rectangle(frame, TARGET_LOCKING_AREA_START_POINT, TARGET_LOCKING_AREA_STOP_POINT,
                  TARGET_LOCKING_AREA_COLOR, 2)
    cv.imshow("CAPTURE", frame)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()