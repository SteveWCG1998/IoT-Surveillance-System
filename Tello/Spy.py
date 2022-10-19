from djitellopy import tello
import KeyPressedModule as kp
from threading import Thread
from time import sleep
import cv2
import time

kp.init()
testfly = tello.Tello()
testfly.connect()
testfly.streamon()

keepRecording = True

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = testfly.get_frame_read().frame.shape
    video = cv2.VideoWriter(f'Resources/{time.time()}.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(testfly.get_frame_read().frame)
        time.sleep(1 / 30)

    video.release()

def getKeyboardInput():
    lr, fb , ud , yv = 0,0,0,0
    speed = 50
    
    if kp.getKey("LEFT"):
        lr = -speed 
    elif kp.getKey("RIGHT"):
        lr = speed

    elif kp.getKey("UP"):
        fb = speed 
    elif kp.getKey("DOWN"):
        fb = -speed

    elif kp.getKey("w"):
        ud = speed 
    elif kp.getKey("s"):
        ud = -speed

    elif kp.getKey("a"):
        yv = speed 
    elif kp.getKey("d"):
        yv = -speed

    if kp.getKey("q"):
        testfly.land()
        sleep(3)
    if kp.getKey("e"):
        testfly.takeoff()  

    if kp.getKey("z"):
        cv2.imwrite(f"Resources/{time.time()}.jpg",testfly.get_frame_read().frame)#img
        time.sleep(0.3)
    
    if kp.getKey("k"):
        recorder = Thread(target=videoRecorder)
        recorder.start()
    elif kp.getKey("l"):
        global keepRecording
        keepRecording = False

    return [lr,fb,ud,yv]



while True:
    vals = getKeyboardInput()
    testfly.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    img = testfly.get_frame_read().frame #live stream
    img = cv2.resize(img,(360,240)) #small means faster
    cv2.imshow("Image",img)
    cv2.waitKey(1) #in case the stream shut down 
    

    
