import json
import uuid

def treat_t_apdu(t_apdu, timestamp, response=False):
    global transaction_data

    if response:
        transaction_data['last_update_timestamp'] = timestamp
        transaction_data['exchanged_data'][-1] |= t_apdu
        return

    if 'initialisationRequest' in t_apdu:
        if 'transaction_data' in globals():
            with open(f'local_file_storage/20241210_transactions/{transaction_data['_id']}.json', 'w') as json_file:
                json.dump(transaction_data, json_file, indent=2)
        transaction_data = {}
        current_transaction_id = uuid.uuid1()
        transaction_data['_id'] = current_transaction_id.hex

        transaction_data['creation_time'] = timestamp
        transaction_data['last_update_timestamp'] = timestamp

        transaction_data |= t_apdu
    elif 'initialisationResponse' in t_apdu:
        transaction_data['last_update_timestamp'] = timestamp
        transaction_data |= t_apdu
        transaction_data['exchanged_data'] = []
    else:
        transaction_data['last_update_timestamp'] = timestamp
        transaction_data['exchanged_data'].append(t_apdu)

    return

with open("beacon_logs/241210_beacon_manager.log", 'r') as logs_file:
    current_json_lines = ''
    json_reading = False
    response = False

    logs_file_iter = iter(logs_file)
    for line in logs_file_iter:
        # if '2024-12-10 10:47:52,815' in line:
        #     exit()
        if json_reading:
            current_json_lines += line
            if line == "]\n" or line == '}\n':
                # print(current_json_lines)
                t_apdu = json.loads(current_json_lines)
                treat_t_apdu(t_apdu, timestamp=timestamp, response=response)
        
        if 'T-APDU in JER:' in line or 'T_APDU containing BST in JER' in line or 'T_APDU containing VST in JER' in line:
            json_reading = True
            timestamp = line[:24]
            json_opener = next(logs_file_iter)[-2:]
            current_json_lines = json_opener
            response = False
        elif 'Response T-APDU decoded with JER:' in line:
            json_reading = True
            timestamp = line[:24]
            json_opener = next(logs_file_iter)[-2:]
            current_json_lines = json_opener
            response = True
        elif "2024-12-10" in line:
            json_reading = False
            current_json_lines = ''
            response = False