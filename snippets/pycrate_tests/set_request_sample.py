from ASN.compiled_DSRC_instances import AXXESv1_2

access_credentials = b'1234'

AXXESv1_2.EfcDsrcGeneric.EfcContainer.from_uper(bytes.fromhex('3150'))
attr_17_val = AXXESv1_2.EfcDsrcGeneric.EfcContainer._val
print(attr_17_val)

set_req_value = {
    'eid': 2,
    'mode': True,
    'accessCredentials': access_credentials,
    'attrList': [
        {'attributeId': 17, 'attributeValue': attr_17_val}
    ],
    'fill': (0, 1)
}
AXXESv1_2.EfcDsrcGeneric.T_APDUs.set_val(('set-request', set_req_value))
print(AXXESv1_2.EfcDsrcGeneric.T_APDUs._val)