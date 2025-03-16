from ASN.compiled_DSRC_instances import OPS1955
# from ASN.compiled_DSRC_asn_files import OPS1955
forced_release_val = {
    'application-id': 12,
    'link-id': 12
}
print('\n\nForced Release example')
OPS1955.KapschOps1955Message.Forced_Release.set_val(forced_release_val)

# print(OPS1955.KapschOps1955Message.Forced_Release._root)
print(OPS1955.KapschOps1955Message.Forced_Release.to_asn1())
print(OPS1955.KapschOps1955Message.Forced_Release.to_uper().hex().upper())
print(OPS1955.KapschOps1955Message.Forced_Release.to_aper().hex().upper())


print('\n\nForced Release message (tag 18) example')
OPS1955.KapschOps1955Message.Message_Types.set_val(('forced-release', forced_release_val))

print(OPS1955.KapschOps1955Message.Message_Types.to_asn1())
print(OPS1955.KapschOps1955Message.Message_Types.to_uper().hex().upper())
print(OPS1955.KapschOps1955Message.Message_Types.to_aper().hex().upper())



trx_status_val = {
    'instance': 1,
    'status': [0xC, 0x8],
    'trx-mode': 0
}
print('\n\nTRX status example')
OPS1955.KapschOps1955Message.TRX_Status.set_val(trx_status_val)

# print(OPS1955.KapschOps1955Message.TRX_Status._root)
print(OPS1955.KapschOps1955Message.TRX_Status.to_asn1())
print(OPS1955.KapschOps1955Message.TRX_Status.to_uper().hex().upper())
print(OPS1955.KapschOps1955Message.TRX_Status.to_aper().hex().upper())

print('TRX Status message (tag 1401) example')
OPS1955.KapschOps1955Message.Message_Types.set_val(('trx-status', trx_status_val))

print(OPS1955.KapschOps1955Message.Message_Types.to_asn1())
print(OPS1955.KapschOps1955Message.Message_Types.to_uper().hex().upper())
print(OPS1955.KapschOps1955Message.Message_Types.to_aper().hex().upper())

print('Read BST config message (tag 2458) example')

MAX_NO_OF_OCTETS = 127
parameter_str = b'Hello World!'
fixed_size_parameter_str = parameter_str +b'\x00' * (MAX_NO_OF_OCTETS-1)
parameter_val = ('octetstring', fixed_size_parameter_str)

MAX_NO_OF_ATTRIBUTES = 16
bst_config_val = {
    'message-status': 0,
    'beacon': {
        'manufacturer-id': 1,
        'individual-id': 2
    },
    'profile': 0,
    'mandatory-application-list':[
        {
            'aid': 1,
            'eid': 1,
            'parameter': parameter_val
        }
    ] * MAX_NO_OF_ATTRIBUTES
}
print(OPS1955.KapschOps1955Message.Message_Types._root.index('bst-configuration2'))


OPS1955.KapschOps1955Message.Message_Types.set_val(('bst-configuration2', bst_config_val))
print(OPS1955.KapschOps1955Message.Message_Types.to_asn1())
print(OPS1955.KapschOps1955Message.Message_Types.to_uper().hex().upper())

uper_encoded_bst_config = b'\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(len(uper_encoded_bst_config))

OPS1955.KapschOps1955Message.BST_Configuration.from_aper(buf = uper_encoded_bst_config)
bst_config_val = OPS1955.KapschOps1955Message.BST_Configuration._val
OPS1955.KapschOps1955Message.Message_Types.set_val(('bst-configuration2', bst_config_val))


print(OPS1955.KapschOps1955Message.Message_Types.to_asn1())



uper_data = bytes.fromhex("010C08000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")

OPS1955.KapschOps1955Message.TRX_Status.from_aper(uper_data)
print(OPS1955.KapschOps1955Message.TRX_Status.to_asn1())