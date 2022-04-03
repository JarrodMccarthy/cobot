from pymycobot import MyCobot
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#Commands for Mosquitto
#start the broker: moquitto -v
#mosquitto_pub -h 192.168.20.30 -t test -m "Hello" - run on server
#mosquitto_sub -v -t "#" - run on client

mc = MyCobot("/dev/ttyAMA0", 1000000)

startposition = [0, -15, 0, 0, 0, 0]
bin1 = [115, 10, -100, 5, 0, 0]
bin2 = [80, -10, -80, 5, 0, 0]
bin3 = [50, -45, -37, 10, 0, 0]
bin4 = [0, -15, 0, 0, 0, 0]

pickup_1 = [10, -50, -90, 35, 0, 0]

pumppin = 9
solpin = 25



shortsleep = 0.5


def send_to_start(mc):
    mc.send_angles(startposition, 50)
    time.sleep(shortsleep)
    return

def send_to_bin(mc, binpos):
    mc.send_angles(binpos, 50)
    time.sleep(shortsleep)
    return 

def solenoid_on(solpin):
    GPIO.setup(solpin, GPIO.OUT)
    GPIO.output(solpin, True)
    return

def solenoid_off(solpin):
    GPIO.setup(solpin, GPIO.IN)
    return

def pump_on(pumppin):
    GPIO.setup(pumppin, GPIO.OUT)
    GPIO.output(pumppin, True)
    return

def pump_off(pumppin):
    GPIO.setup(pumppin, GPIO.IN)
    #GPIO.output(pumppin, False)
    return

send_to_start(mc)

mc.send_angles(pickup_1, 40)
time.sleep(2)

pump_on(pumppin)
solenoid_on(solpin)
time.sleep(2)
send_to_start(mc)

send_to_bin(mc, bin2)
time.sleep(2)

pump_off(pumppin)
solenoid_off(solpin)
time.sleep(2)

send_to_start(mc)
time.sleep(2)
