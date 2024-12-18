from ASN.compiled_DSRC_instances import CCCv4_1 as EFC
import datetime

EFC.EfcCcc.CccContainer.from_uper(bytes.fromhex("6403FF6760334130CC14440321339801FF67602F5603CC144903213388"))

print(EFC.EfcCcc.CccContainer.to_asn1())
attr_100_jval = EFC.EfcCcc.CccContainer._to_jval()

utc_ts = attr_100_jval['extendedObeStatusHistoryPart2']['timeWhenChangedToPrevious2']

print(datetime.datetime.fromtimestamp(utc_ts, datetime.UTC))