import cv2

print(cv2.__version__)
dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
BW=int(.2*dispW)
BH=int(.2*dispH)
posX=10
posY=180
dx=2
dy=2

#Or, if you have a WEB cam, uncomment the next line
#(If it does nqot work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    roi=frame[posY:posY+BH,posX:posX+BW].copy()
    
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()