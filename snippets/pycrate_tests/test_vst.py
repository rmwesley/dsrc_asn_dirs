from ASN.compiled_DSRC_instances import EFCv10_1 as EFC


# fragmented_t_apdu_with_vst = bytes.fromhex("91900001C1040206B2803100097C801300290000")
t_apdu_with_vst = bytes.fromhex("900001C1040206B2803100097C801300290000")

EFC.EfcDsrcGeneric.T_APDUs.from_uper(t_apdu_with_vst)
print(EFC.EfcDsrcGeneric.T_APDUs.to_jer())
print(EFC.EfcDsrcGeneric.T_APDUs.to_asn1())
print(EFC.EfcDsrcGeneric.T_APDUs._val)

vst_parameter = EFC.EfcDsrcGeneric.T_APDUs._val[1]['applications'][0]['parameter']
print(vst_parameter)

EFC.EfcDsrcGeneric.EfcContainer.set_val(vst_parameter)
print(EFC.EfcDsrcGeneric.EfcContainer._val)
print(EFC.EfcDsrcGeneric.EfcContainer._val[1].hex())