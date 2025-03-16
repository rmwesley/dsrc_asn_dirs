from ASN.compiled_DSRC_instances import EFCv10_1 as EFC

EFC.EfcDsrcGeneric.EfcContainer.from_uper(bytes.fromhex("362708002F"))
# EFC.EfcDsrcGeneric.EfcContainer.from_uper(bytes.fromhex("3670FF0230"))
"3670FF0230"

print(EFC.EfcDsrcGeneric.EfcContainer.to_asn1())
print(EFC.EfcDsrcGeneric.EfcContainer.to_jer())