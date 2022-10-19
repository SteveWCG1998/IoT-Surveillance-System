from djitellopy import tello
import cv2

TestFly = tello.Tello()
TestFly.connect()
print(TestFly.get_battery())

TestFly.streamon()

while True:
    img = TestFly.get_frame_read().frame
    #img = cv2.resize(img(360,240)) #small means faster
    cv2.imshow("Image",img)
    cv2.waitKey(1) #in case the stream shut down 