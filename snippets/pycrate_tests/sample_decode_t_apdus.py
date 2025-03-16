from ASN.compiled_DSRC_instances import LACv2_1

# paymeans_hex = "403156496000311004541F577E0000"
# paymeans_bytes = bytes.fromhex(paymeans_hex)
# LACv2_1.EfcCcc.CccContainer.from_uper(paymeans_bytes)
# print(LACv2_1.EfcCcc.CccContainer.to_asn1())

fragmented_t_apdu_with_get_response_hex = "911405120120403156496000311004541F577E0000047E9CB574"
# fragmented_t_apdu_with_get_response_hex = "9114051201403156496000311004541F577E0000047E9CB574"
fragmented_t_apdu_with_get_response_bytes = bytes.fromhex(fragmented_t_apdu_with_get_response_hex)

CHECK_T_APDU = True
if CHECK_T_APDU == True:
    t_apdu_with_response_bytes = bytes(fragmented_t_apdu_with_get_response_bytes[1:])
    print(t_apdu_with_response_bytes.hex().upper())

    LACv2_1.EfcDsrcGeneric.T_APDUs.from_uper(t_apdu_with_response_bytes)
    print(LACv2_1.EfcDsrcGeneric.T_APDUs.to_asn1())

    LACv2_1.EfcCcc.CccTApdus.from_uper(t_apdu_with_response_bytes)
    print(LACv2_1.EfcCcc.CccTApdus.to_asn1())

CHECK_ACTION_RESPONSE = False
if CHECK_ACTION_RESPONSE:
    action_response_bytes = bytes.fromhex(fragmented_t_apdu_with_get_response_hex[3:] + "0")
    print(action_response_bytes.hex().upper())

    LACv2_1.EfcDsrcGeneric._T_APDUs_action_response.from_uper(action_response_bytes)
    print(LACv2_1.EfcDsrcGeneric._T_APDUs_action_response.to_asn1())

    # LACv2_1.EfcCcc._CccTApdus_actionResponse.from_uper(action_response_bytes)
    # print(LACv2_1.EfcCcc._CccTApdus_actionResponse.to_asn1())
    LACv2_1.EfcCcc.CccAuthDataRetrievalResponse.from_uper(action_response_bytes)
    print(LACv2_1.EfcCcc.CccAuthDataRetrievalResponse.to_asn1())