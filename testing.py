from pymycobot import MyCobot

mc = MyCobot("/dev/ttyAMA0", 1000000)

print(mc.get_angles())

print(mc.get_coords())