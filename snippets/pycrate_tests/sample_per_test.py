from ASN import PER_TEST

content_val = 0x7B #  123

PER_TEST.PerTest.BigContainer.set_val(('indicator0', content_val))
# print(PER_TEST.PerTest.BigContainer._root)
print(PER_TEST.PerTest.BigContainer.to_asn1())
print(PER_TEST.PerTest.BigContainer.to_uper().hex().upper())
print(PER_TEST.PerTest.BigContainer.to_aper().hex().upper())


PER_TEST.PerTest.BigContainer.set_val(('indicator40', content_val))
# print(PER_TEST.PerTest.BigContainer._root)
print(PER_TEST.PerTest.BigContainer.to_asn1())
print(PER_TEST.PerTest.BigContainer.to_uper().hex().upper())
print(PER_TEST.PerTest.BigContainer.to_aper().hex().upper())

PER_TEST.PerTest.BigContainer.set_val(('indicator80', content_val))
# print(PER_TEST.PerTest.BigContainer._root)
print(PER_TEST.PerTest.BigContainer.to_asn1())
print(PER_TEST.PerTest.BigContainer.to_uper().hex().upper())
print(PER_TEST.PerTest.BigContainer.to_aper().hex().upper())

PER_TEST.PerTest.BigContainer.set_val(('indicator1400', content_val))
# print(PER_TEST.PerTest.BigContainer._root)
print(PER_TEST.PerTest.BigContainer.to_asn1())
print(PER_TEST.PerTest.BigContainer.to_uper().hex().upper())
print(PER_TEST.PerTest.BigContainer.to_aper().hex().upper())


PER_TEST.PerTest.BigContainer.set_val(('indicator2200', content_val))
# print(PER_TEST.PerTest.BigContainer._root)
print(PER_TEST.PerTest.BigContainer.to_asn1())
print(PER_TEST.PerTest.BigContainer.to_uper().hex().upper())
print(PER_TEST.PerTest.BigContainer.to_aper().hex().upper())