import time
import serial
import threading

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM13',
    baudrate=115200,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_TWO
)
if ser.isOpen():
    print('Port open!!')

# Reading the data from the serial port. This will be running in an infinite loop.
def indefinitely_read_rx_buffer():
    while True:
        input_buffer_size = ser.in_waiting
        data = ser.read(input_buffer_size)
        if data != b'':
            print(data)
        time.sleep(0.01)
bac_rx_thread = threading.Thread(target=indefinitely_read_rx_buffer, daemon=True)
bac_rx_thread.start()

time.sleep(0.4)

print('Send CD_READ_TIME')
ser.write(b'\x64')
time.sleep(5)

print('Send CD_MODE STOPPED')
# ser.write(b'\x00\x00')
time.sleep(5)

print('Send CD_MONITOR')
# ser.write(b'\x01')
time.sleep(5)