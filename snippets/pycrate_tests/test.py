from ASN.compiled_DSRC_instances import EFCv10_1 as EFC
import json

json_str = '''
{
 "get-response": {
  "attributelist": [
   {
    "attributeId": 32,
    "attributeValue": {
     "paymeans": {
      "paymentMeansExpiryDate": {
       "day": 31,
       "month": 10,
       "year": 2034
      },
      "paymentMeansUsageControl": "0000",
      "personalAccountNumber": "0f0f0f0f0f0f0f0f0f0f"
     }
    }
   }
  ],
  "eid": 4,
  "fill": "00"
 }
}'''

EFC.EfcDsrcGeneric.T_APDUs.from_jer(json_str)
print(EFC.EfcDsrcGeneric.T_APDUs._val)

beacon_id_hex = "000200000000"
beacon_id_uper = bytes.fromhex(beacon_id_hex)

EFC.EfcDsrcGeneric.BeaconID.from_uper(beacon_id_uper)
print(EFC.EfcDsrcGeneric.BeaconID.to_jer())