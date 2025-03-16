from ASN.compiled_DSRC_instances import EFCv10_1 as EFC

bst_uper = bytes.fromhex("8001880001116786AAED000301141D0100")
EFC.EfcDsrcGeneric.T_APDUs.from_uper(bst_uper)
print(EFC.EfcDsrcGeneric.T_APDUs.to_asn1())