lic_etc_gen_headers_str = """  /* Message ID 0 */
  Action_Request_Type Action_Request;

  /* Message ID 1 */
  Action_Confirmation_Type Action_Confirmation;

  /* Message ID 4 */
  Set_Request_Type Set_Request;

  /* Message ID 5 */
  Set_Confirmation_Type Set_Confirmation;

  /* Message ID 6 */
  Get_Request_Type Get_Request;

  /* Message ID 7 */
  Get_Confirmation_Type Get_Confirmation;

  /* Message ID 12 */
  Notify_Application_Beacon_Type Notify_Application_Beacon;

  /* Message ID 13 */
  Ready_Application_Type Ready_Application;

  /* Message ID 14 */
  Notify_Application_Lost_Message_Type Notify_Application_Lost_Message;

  /* Message 18 */
  Forced_Release_Type Forced_Release;

  /* Message 103, 105 */
  Tis_Ready_Application_Type Tis_Ready_Application;

  /* Message ID 1401 */
  TRX_Status_Type TRX_Status;

  /* Message ID 1402 */
  TRX_ID_Type TRX_ID;

  /* Message ID 1403 */
  TRX_Internal_Humidity_Type TRX_Internal_Humidity;

  /* Message ID 1404 */
  TRX_Internal_Temperature_Type TRX_Internal_Temperature;

  /* Message ID 1405 */
  TRX_My_Power_Mode_Type TRX_My_Power_Mode;

  /* Message ID 1406, 1415 */
  TRX_Carrier_Frequency_Type TRX_Carrier_Frequency;

  /* Message ID 1407 */
  TRX_Uplink_Parameters_Type TRX_Uplink_Parameters;

  /* Message ID 1408, 1416 */
  TRX_Output_Power_Type TRX_Output_Power;

  /* Message ID 1414 */
  TRX_Echo_Type TRX_Echo;

  /* Message ID 1420 */
  TRX_Set_UI_Control_Type TRX_Set_UI_Control;

  /* Message ID 1421 */
  TRX_Read_UI_Control_Type TRX_Read_UI_Control;
  
  /* Message ID 1422, 1423 */
  TRX_UI_Status_Type TRX_UI_Status;

  /* Message ID 1500 */
  TRX_General_Purpose_Type TRX_General_Purpose;

  /* Message ID 1506 */
  TRX_Extended_Output_Power_Type TRX_Extended_Output_Power;

  /* Message ID 1516 */
  TRX_SET_RF_Param_Type TRX_SET_RF_Param;
  
  /* Message ID 1517 */
  TRX_READ_RF_Param_Type TRX_READ_RF_Param;

  /* Message ID 2408 and 2409 */
  Lic_Nalm_Behaviour_Type Lic_Nalm_Behaviour;

  /* Message ID 2410 and 2411 */
  Lic_PDU_No_Behaviour_Type Lic_PDU_No_Behaviour;

  /* Message ID 2412 and 2413 */
  Lic_L7_Ack_Mode_Type Lic_L7_Ack_Mode;

  /* Message ID 2414 and 2415 */
  Lic_Private_Uplink_Window_Time_Type Lic_Private_Uplink_Window_Time;

  /* Message ID 2416 and 2417 */
  Lic_Slow_Data_Behaviour_Type Lic_Slow_Data_Behaviour;

  /* Message ID 2418 and 2419 */
  Lic_Release_Retransmissions_Type Lic_Release_Retransmissions;

  /* Message ID 2420 and 2421 */
  Lic_LID_Cleanup_Mode_Type Lic_LID_Cleanup_Mode;

  /* Message ID 2450 and 2451 */
  DSRC_Link_Mode_Type DSRC_Link_Mode;

  /* Message ID 2455 and 2456*/
  DSRC_Configuration_Type DSRC_Configuration;

  /* Message ID 2457 and 2458 */
  BST_Configuration_Type BST_Configuration;

  /* Message ID 2459 and 2460 */
  Time_Type Time;

  /* Message ID 2463 and 2464 */
  General_Log_Level_Type General_Log_Level;

  /* Message ID 2465 and 2466 */
  Log_Category_Mode_Type Log_Category_Mode;

  /* Message ID 2482 and 2483 */
  Transaction_Status_Type Transaction_Status;

  /* Message ID 2605 */
  Echo_Type Echo;

  /* Message ID 2650 */
  Communication_Log_Result_Type Communication_Log_Result;

  /* Message ID 2651 and 2752 */
  LiC_Status_Type LiC_Status;

  /* Message ID 2751 */
  LiC_Statistics_Type LiC_Statistics;

  /* Message ID 2753 and 2754 */
  Status_Mode_Type Status_Mode;

  /* Message ID 0,2,4,6,13 */
  DSRC_Return_Status_Type DSRC_Return_Status;

  /* Message ID 2450, 2455, 2457, 2459, 2463, */
  /*            2465, 2467, 2753  */
  uint8_t Return_Status;

  /* Message ID 1400, 1405, 1406, 1407, 1408 */
  /*            1506  */
  TRX_Return_Status_Type TRX_Return_Status;

  /* Message ID 1400 DL */
  uint8_t TRX_Instance;

  /* Message ID 2772 */
  LiC_Version_Type LiC_Version;

"""

class EndOfTypeDefs(Exception):
    pass

def grab_message_ids(line_iter) -> (str, list):
    message_ids = []
    message_type = str()

    for line in line_iter:
        # print(line)
        if line == "":
            if not message_ids:
                raise EndOfTypeDefs("Grabbing over")
            return message_type, message_ids
        elif '/*' in line:
            for word in line.split(" "):
                # print(word)
                if not word:
                    continue
                if word[-1] == ',':
                    word = word[:-1]
                if word.isnumeric():
                    message_id = int(word)
                    message_ids.append(message_id)
        else:
            message_type_with_semicolon = line.split(" ")[-1]
            message_type = message_type_with_semicolon[:-1]

def asn_choice_elements(message_type:str, message_ids:list):
    asn_lines = []
    for message_id in message_ids:
        asn1_identifier = message_type.lower().replace('_', '-')
        message_type = message_type.replace('_', '-')
        asn_lines.append(f"{asn1_identifier} [{message_id}] {message_type},")
    asn_str = "\n".join(asn_lines)
    return asn_str

if __name__ == "__main__":
    lines_iter = iter(lic_etc_gen_headers_str.split("\n"))

    while True:
        try:
            message_type, message_ids = grab_message_ids(lines_iter)
            # print(message_type, message_ids)
            asn_str = asn_choice_elements(message_type, message_ids)
            print(asn_str)
        except EndOfTypeDefs:
            exit(0)