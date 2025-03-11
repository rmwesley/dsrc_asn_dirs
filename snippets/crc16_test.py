def crc16_arc(data : bytearray):
    crc = 0
    for byte_val in data:
        crc ^= byte_val
        for j in range(8):
            if ((crc & 0x1) == 1):
                crc = int((crc / 2)) ^ 40961
            else:
                crc = int(crc / 2)
    return crc & 0xFFFF

message_frame = bytes.fromhex('01 10 03')
msg_crc16 = crc16_arc(message_frame)
crc16_bytes = int.to_bytes(msg_crc16, length=2, byteorder='little')
print(crc16_bytes.hex())