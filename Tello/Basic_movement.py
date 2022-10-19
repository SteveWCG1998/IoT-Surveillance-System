from djitellopy import tello
from time import sleep

TestFly = tello.Tello()
TestFly.connect()
TestFly.enable_mission_pads()
TestFly.set_mission_pad_detection_direction(1)

TestFly.takeoff()
print(TestFly.get_mission_pad_id())
TestFly.land()

#TestFly.send_read_command("sdk?")



TestFly.takeoff()
sleep(1)
TestFly.send_rc_control(0,0,20,0)
sleep(1)

sleep(1)
print(TestFly.get_height())
sleep(1)
TestFly.send_rc_control(0,0,-20,0)
sleep(1)
TestFly.land()