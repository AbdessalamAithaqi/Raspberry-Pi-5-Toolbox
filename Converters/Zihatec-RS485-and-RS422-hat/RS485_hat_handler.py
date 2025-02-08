import serial
from  time import sleep

rs485hat = serial.Serial(port='/dev/serial0', baudrate=9600, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

while True:
    rs485hat.write(b"Testing")
    print("message sent")
    sleep(1)