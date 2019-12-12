import cv2 as cv

PAL_WIDTH = 720
PAL_HEIGHT = 576
NTSC_WIDTH = 640
NTSC_HEIGHT = 480
# fsdvfgsd
TARGET_LOCKING_AREA_STOP_POINT = int(((NTSC_WIDTH / 100) * 25)), int(((NTSC_HEIGHT / 100) * 10))
TARGET_LOCKING_AREA_START_POINT = int(((NTSC_WIDTH / 100) * 75)), int(((NTSC_HEIGHT / 100) * 90))
TARGET_LOCKING_AREA_COLOR = (0, 0, 255)
capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, NTSC_WIDTH)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, NTSC_HEIGHT)
while True:

    ret, frame = capture.read()
    width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print("size", width, height)
    cv.rectangle(frame, TARGET_LOCKING_AREA_START_POINT, TARGET_LOCKING_AREA_STOP_POINT, TARGET_LOCKING_AREA_COLOR, 2)
    cv.imshow("CAPTURE GRAY", gray)
    cv.imshow("CAPTURE", frame)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()