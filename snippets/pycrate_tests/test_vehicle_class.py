from ASN.compiled_DSRC_instances import EFCv10_1 as EFC

# EFC.EfcDsrcGeneric.EfcContainer.from_uper(b"\x31\xD0")

# print(EFC.EfcDsrcGeneric.EfcContainer.to_asn1())

EFC.EfcDsrcGeneric.EfcContainer.from_uper(bytes.fromhex("36F01C0034"))
print(EFC.EfcDsrcGeneric.EfcContainer.to_asn1())
# print(EFC.EfcDsrcGeneric.EfcContainer.to_jer())

# EFC.EfcDsrcGeneric.EfcContainer.from_uper(bytes.fromhex("3660040324"))
# print(EFC.EfcDsrcGeneric.EfcContainer.to_asn1())
# print(EFC.EfcDsrcGeneric.EfcContainer.to_jer())