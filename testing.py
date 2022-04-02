from pymycobot import MyCobot

mc = MyCobot("/dev/ttyAMA0", 1000000)



def send_to_start(mc):
    mc.send_angles([0, -100, 0, 0, 0, 0], 50)
    return

print(mc.get_angles())
print(mc.get_coords())
send_to_start(mc)
print(mc.get_angles())
