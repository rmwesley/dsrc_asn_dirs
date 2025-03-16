from ASN.compiled_DSRC_instances import AXXESv1_1 as EFC_CCC_LAC_asn1_objs

# efc_cm_uper_bytes = bytes.fromhex('B28031000A8D')
# EFC_CCC_LAC_asn1_objs.EfcDataDictionary.EfcContextMark.from_uper(efc_cm_uper_bytes)

efc_cm_val = {
    'contractProvider': {
        'countryCode': (714, 10),
        'providerIdentifier': 0x31
    },
    'typeOfContract': bytes.fromhex('000A'),
    'contextVersion': 141
}

EFC_CCC_LAC_asn1_objs.EfcDataDictionary.EfcContextMark.set_val(efc_cm_val)
efc_cm_uper_val = EFC_CCC_LAC_asn1_objs.EfcDataDictionary.EfcContextMark.to_uper()
print(efc_cm_uper_val.hex().upper())