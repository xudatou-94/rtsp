
#url rtsp://192.168.2.20:554/user=admin&password=&channel=1&stream=0.sdp?real_stream
import cv2
cap = cv2.VideoCapture("rtsp://192.168.2.20:554/user=admin&password=&channel=2&stream=0.sdp?real_stream")
print(cap.isOpened())
ret,frame = cap.read()
print(ret)
while ret:
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
