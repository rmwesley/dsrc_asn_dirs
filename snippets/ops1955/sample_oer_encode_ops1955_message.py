from ASN.compiled_DSRC_instances import OPS1955

message_id = 2460
# choice_identifier = OPS1955.KapschOps1955Message.KapschResponseMessages._cont_tags[(2, message_id)]
# cont_type = OPS1955.KapschOps1955Message.KapschResponseMessages._cont[choice_identifier]
# print(cont_type)

cont_type = OPS1955.KapschOps1955Message.KapschTime

cont_val = {
    'message-status': 0,
    'unix-time': 0xC4,
    'milliseconds': 0x6900
}
cont_type.set_val(cont_val)
print(cont_type.to_oer().hex().upper())

message_cont = bytes.fromhex("00000000C46900")
cont_type.from_oer(message_cont)
print(cont_type.to_asn1())