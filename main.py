from cobs import cobs
import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=3)

zeroByte = b'\x00'  # COBS 1-byte delimiter is hex zero as a (binary) bytes character


def write_robot(left: float, right: float):
    values = cobs.encode(int(left * 127).to_bytes(1, byteorder='big', signed=True) +
                         int(right * 127).to_bytes(1, byteorder='big', signed=True))

    ser.write(values + b'\0')


while True:
    write_robot(1, 1)
    sleep(1)
    write_robot(0, 0)
    sleep(1)
    write_robot(-1, -1)
    sleep(1)

