from ASN.compiled_DSRC_instances import EFCv10_1 as EFC

json = {
 "vehspchars": {
  "descriptiveCharacteristics": 0,
  "engineCharacteristics": 8,
  "environmentalCharacteristics": {
   "copValue": 7,
   "euroValue": 2
  },
  "futureCharacteristics": {
   "co2Class": 3,
   "co2Scheme": 1,
   "futureElement": 0,
   "suspensionType": 3
  }
 }
}

EFC.EfcDsrcGeneric.EfcContainer._from_jval(json)
print(EFC.EfcDsrcGeneric.EfcContainer.to_uper().hex().upper())

# EFC.EfcDsrcGeneric.EfcContainer.from_uper(bytes.fromhex("3660040324"))
# print(EFC.EfcDsrcGeneric.EfcContainer.to_asn1())
# print(EFC.EfcDsrcGeneric.EfcContainer.to_jer())