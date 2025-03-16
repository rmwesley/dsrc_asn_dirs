import asyncio
from serial_asyncio import open_serial_connection
import time
import threading
import os

# Reading the data from the serial port.
# This is a coroutine running in an infinite loop, awaiting one line at a time.
async def read_line(reader : asyncio.StreamReader):
    while True:
        # print(reader._buffer)
        line = await reader.readline()
        print(f"Received bytes data!: {line}")
        # print(str(line, 'utf-8'))

loop = asyncio.new_event_loop()

def indefinitely_read_rx_buffer(reader : asyncio.StreamReader):
    bac_rx_thread = threading.Thread(target=loop.run_until_complete, args=[read_line(reader=reader)], daemon=True)
    bac_rx_thread.start()

# Initializing BAC
reader, writer = loop.run_until_complete(
    open_serial_connection(url='COM15', baudrate=115200, parity='E', stopbits=2, limit=256)
)

indefinitely_read_rx_buffer(reader=reader)
time.sleep(1)

print('Send CD_MONITOR')
response = writer.write(b'\x01')
os.urandom(4)
print('Wrote 0x01')
time.sleep(0.2)

loop_writes = False
while loop_writes:
    print('Send random command')
    request = os.urandom(1)
    response = writer.write(request)
    print(f'Wrote {request.hex().upper()}')
    time.sleep(0.4)
# print('Send CD_READ_TIME')
# writer.write(b'\x64')
# print('Wrote 0x64')
time.sleep(15)

# loop = asyncio.new_event_loop()
# loop.run_until_complete(run())