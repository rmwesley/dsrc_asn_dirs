import ASN.compiled_DSRC_instances.EFCv10_1 as EFC

# data = bytes.fromhex("403156495005846000782F591F0000")
# data = bytes.fromhex("403156490085210000415F593E0000")
data = bytes.fromhex("403156490085210000415F456F0000")
EFC.EfcDsrcGeneric.EfcContainer.from_uper(data)
print(EFC.EfcDsrcGeneric.EfcContainer._val)

data = bytes.fromhex("403156490085210000415F593E0000")
EFC.EfcDsrcGeneric.EfcContainer.from_uper(data)
print(EFC.EfcDsrcGeneric.EfcContainer._val)
print(EFC.EfcDsrcGeneric.EfcContainer.to_jer())