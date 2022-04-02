from pymycobot import MyCobot
import time

mc = MyCobot("/dev/ttyAMA0", 1000000)

startposition = [0, -15, 0, 0, 0, 0]
bin1 = [0, -15, 0, 0, 0, 0]
bin2 = [0, -15, 0, 0, 0, 0]
bin3 = [0, -15, 0, 0, 0, 0]
bin4 = [0, -15, 0, 0, 0, 0]
shortsleep = 0.1

def send_to_start(mc):
    mc.send_angles(startposition, 50)
    time.sleep(shortsleep)
    return

def send_to_bin(mc, binpos):
    mc.send_angles(binpos, 50)
    time.sleep(shortsleep)
    return 

def grab_item():
    pass


send_to_start(mc)


