from pymycobot import MyCobot

mc = MyCobot("/dev/ttyAMA0", 1000000)

mc.get_angles()