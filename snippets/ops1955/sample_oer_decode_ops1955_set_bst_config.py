from ASN.compiled_DSRC_instances import OPS1955

# No such thing as a NULL unconstrained INT!
# a = OPS1955.INT()
# a.set_val(0)
# print(a.to_oer())
# print(a.to_coer())
# print(a.to_oer_ws())
# print(a.to_uper())

# message_id = 2457
# raw_obe_setup_lib_ops1955_bst_config = bytes.fromhex('0000000001000000A3000000010000001D')
# bst_config_val = raw_obe_setup_lib_ops1955_bst_config
# # bst_config_val = bytes.fromhex('00 0001 000000B7 00 010001')
# OPS1955.KapschOps1955Message._KapschRequestMessages_set_bst_configuration.from_oer(bst_config_val)
# print(OPS1955.KapschOps1955Message._KapschRequestMessages_set_bst_configuration.to_asn1())

mandApplications = [{'aid':29, 'unknown': 0}]
# mandApplications = [{'parameter': ('octetstring', b'\x00'), 'aid':1}]

bst_config_value = {
    'message-status': 0,
    'rsu': {
        'manufacturerid': 1,
        'individualid': 0xB7
        },
    'profile': 0x7F,
    'mandApplications': mandApplications,
    'nonMandApplications': [],
    'profileList': [],
    'unknown1': 0,
    'unknown2': 0,
    'unknown3': 0,
    'unknown4': 0
    }
OPS1955.KapschOps1955Message.KapschRequestMessages.set_val(('set-bst-configuration', bst_config_value))
print(OPS1955.KapschOps1955Message.KapschRequestMessages.to_asn1())
print(OPS1955.KapschOps1955Message.KapschRequestMessages.to_oer().hex().upper())
print(OPS1955.KapschOps1955Message._KapschRequestMessages_set_bst_configuration.to_oer().hex().upper())
# print(OPS1955.KapschOps1955Message._KapschRequestMessages_set_bst_configuration.to_coer().hex().upper())
print(OPS1955.KapschOps1955Message._KapschRequestMessages_set_bst_configuration.to_aper().hex().upper())

my_list = OPS1955.EfcDsrcGeneric.AttributeIdList
my_list.set_val([0, 1, 4, 3])
print(my_list.to_oer().hex().upper())
# print(my_list.to_coer().hex().upper())
print(my_list.to_uper().hex().upper())
# my_list_type.set_val([{'field1': (1, 0)}, {'field1': (2, 0xFFF)}])