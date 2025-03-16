import ASN.compiled_DSRC_instances.CCCv4_1 as EFC

# data = bytes.fromhex("403156495005846000782F591F0000")
# data = bytes.fromhex("403156490085210000415F593E0000")
data = bytes.fromhex("403156490085210000415F456F0000")
EFC.EfcDsrcGeneric.EfcContainer.from_uper(data)
# print(EFC.EfcDsrcGeneric.EfcContainer._val)

data = bytes.fromhex("403156490085210000415F593E0000")
EFC.EfcDsrcGeneric.EfcContainer.from_uper(data)
# print(EFC.EfcDsrcGeneric.EfcContainer._val)
# print(EFC.EfcDsrcGeneric.EfcContainer.to_jer())


extended_obe_status_hist_part1_bytes_uper = bytes.fromhex('0067373A7733000000000000000001673736C836004A112A02BA3D586737380800000000')
EFC.EfcCcc.ExtendedObeStatusHistoryPart1.from_uper(extended_obe_status_hist_part1_bytes_uper)

print("ExtendedObeStatusHistoryPart1:")
# print(EFC.EfcCcc.ExtendedObeStatusHistoryPart1.to_jer())
print(EFC.EfcCcc.ExtendedObeStatusHistoryPart1.to_asn1() + "\n\n")


print("ExtendedObeStatusHistoryPart2:")
extended_obe_status_hist_part2_bytes_uper = bytes.fromhex('0067372A1130000000000000000001673724DA02004A15C402BA3F48')
EFC.EfcCcc.ExtendedObeStatusHistoryPart2.from_uper(extended_obe_status_hist_part2_bytes_uper)
# print(EFC.EfcCcc.ExtendedObeStatusHistoryPart2.to_jer())
print(EFC.EfcCcc.ExtendedObeStatusHistoryPart2.to_asn1() + "\n\n")