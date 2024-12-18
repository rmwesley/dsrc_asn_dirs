import json
import uuid

local_transactions_storage_path = 'local_file_storage/20241206_transactions'
beacon_logs_filepath = "beacon_logs/241206_beacon_manager.log"

def treat_t_apdu(t_apdu, timestamp, response=False):
    global transaction_data
    # print(t_apdu)

    if 'initialisationRequest' in t_apdu:
        if 'transaction_data' in globals():
            with open(f'{local_transactions_storage_path}/{transaction_data['_id']}.json', 'w') as json_file:
                json.dump(transaction_data, json_file, indent=2)
        transaction_data = {}
        current_transaction_id = uuid.uuid1()
        transaction_data['_id'] = current_transaction_id.hex

        transaction_data['creation_time'] = timestamp
        transaction_data['last_update_timestamp'] = timestamp

        transaction_data |= t_apdu
    elif 'transaction_data' not in globals():
        print('FIXME: Transaction data not kept because another transaction was tried to be initialized!')
        return
    elif response:
        transaction_data['last_update_timestamp'] = timestamp
        transaction_data['exchanged_data'][-1] |= t_apdu
        return
    elif 'initialisationResponse' in t_apdu:
        transaction_data['last_update_timestamp'] = timestamp
        transaction_data |= t_apdu
        transaction_data['exchanged_data'] = []
    else:
        if 'exchanged_data' not in transaction_data:
            print(transaction_data)
            print(t_apdu)
        transaction_data['last_update_timestamp'] = timestamp
        transaction_data['exchanged_data'].append(t_apdu)

    return

def read_json(logs_file_iter, response):
    json_opener_with_newline = next(logs_file_iter)[-2:]
    current_json_lines = json_opener_with_newline
    for line in logs_file_iter:
        current_json_lines += line

        if line == "]\n" or line == '}\n':
            # print(current_json_lines)
            t_apdu = json.loads(current_json_lines)
            treat_t_apdu(t_apdu, timestamp=timestamp, response=response)
        elif "2024-12-06" in line:
            return

with open(beacon_logs_filepath, 'r') as logs_file:
    logs_file_iter = iter(logs_file)
    for line in logs_file_iter:
        # if '2024-12-10 10:47:52,815' in line:
        #     exit()
        if 'ERROR' in line:
            print('ERROR mid-transaction!!')
            if 'transaction_data' in globals():
                del transaction_data

        if 'T_APDU containing BST in JER' in line:
            timestamp = line[:23]
            read_json(logs_file_iter=logs_file_iter, response=False)
        if 'T-APDU in JER:' in line or 'T_APDU containing VST in JER' in line:
            timestamp = line[:23]
            read_json(logs_file_iter=logs_file_iter, response=False)
        elif 'Response T-APDU decoded with JER:' in line:
            timestamp = line[:23]
            read_json(logs_file_iter=logs_file_iter, response=True)