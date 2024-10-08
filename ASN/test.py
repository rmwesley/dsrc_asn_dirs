# from compiled_DSRC_instances.CCCv4_1 import EfcDsrcGeneric, EfcDataDictionary
from compiled_DSRC_instances.EFCv10_1 import EfcDsrcGeneric, EfcDataDictionary

BeaconID = EfcDsrcGeneric.BeaconID
BeaconID.set_val({
  'manufacturerid': 0x1,
  'individualid': 1052 #41C
  })
print(BeaconID.to_asn1())
print("BeaconID UPER:", BeaconID.to_uper().hex().upper())
BST = EfcDsrcGeneric.BST
utc_ts = 1103790512

bst_value = {
  'rsu': {
    'manufacturerid': 0x1,
    'individualid': 1052 #41C
    },
  'time':utc_ts,
  'profile': 0,
  'mandApplications': [
    {
    'aid': 3
    }
    ],
  'profileList': []
  }
BST.set_val(bst_value)

print(f"BST encoded in UPER in hex: {BST.to_uper().hex().upper()}")
print()

contract_provider = "30C001"
toc = 0x0001
cv = 0x02
efc_cm_str = f"{contract_provider}{toc:04X}{cv:02X}"
print(f"EFC-CM: {efc_cm_str}")
EfcContextMark = EfcDataDictionary.EfcContextMark
EfcContextMark.from_uper(bytes.fromhex(f"{efc_cm_str}"))
print("EFC-CM from UPER encoding in JER:", EfcContextMark.to_jer())
efc_cm = {
  'contractProvider': {
    'countryCode': (195, 10),
    'providerIdentifier': 1
    },
  'typeOfContract': b'\x00\x01',
  'contextVersion': 2
  }

EfcContextMark.set_val(efc_cm)
print(EfcContextMark.to_asn1())
print("EFC-CM in UPER encoding:", EfcContextMark.to_uper().hex().upper())

EfcContainer = EfcDsrcGeneric.EfcContainer
EfcContainer.set_val(('efccontext', EfcContextMark._val))
print(EfcContainer.to_asn1())

EfcContainer.set_val(('attrList', [
  {
  'attributeId': 0,
  'attributeValue': ('octetstring', bytes.fromhex(efc_cm_str))
  }
]))
print("EFC Container with AttrList encoded in UPER in hex:", EfcContainer.to_uper().hex().upper())
print(EfcContainer.to_asn1())