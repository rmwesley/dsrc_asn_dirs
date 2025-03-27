from ASN.compiled_DSRC_instances import AXXESv1_2 as efc_asn_compilation

# efc_cm_uper_bytes = bytes.fromhex('B28031000A8D')
# efc_asn_compilation.EfcDataDictionary.EfcContextMark.from_uper(efc_cm_uper_bytes)

efc_cm_val = {
    'contractProvider': {
        'countryCode': (714, 10),
        'providerIdentifier': 0x31
    },
    'typeOfContract': bytes.fromhex('000A'),
    'contextVersion': 141
}

efc_asn_compilation.EfcDataDictionary.EfcContextMark.set_val(efc_cm_val)
efc_cm_uper_val = efc_asn_compilation.EfcDataDictionary.EfcContextMark.to_uper()
print(efc_cm_uper_val.hex().upper())