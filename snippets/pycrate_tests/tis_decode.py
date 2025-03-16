from ASN.compiled_DSRC_instances import AXXES

AXXES.EfcTisCipCardme.TisContainer.from_uper(bytes.fromhex('6102083E812DCEAC000200'))
print(AXXES.EfcTisCipCardme.TisContainer.to_asn1())
AXXES.EfcTisCipCardme.TisContainer.from_uper(bytes.fromhex('620206001600040800'))
print(AXXES.EfcTisCipCardme.TisContainer.to_asn1())

AXXES.EfcTisCipCardme.TisContainer.from_uper(bytes.fromhex('63F000000000000000000000000000'))
print(AXXES.EfcTisCipCardme.TisContainer.to_asn1())