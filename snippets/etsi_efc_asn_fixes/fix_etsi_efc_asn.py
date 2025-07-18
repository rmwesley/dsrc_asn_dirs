def fix_etsi_asn_txt_sequence_fixed_field_values(asn_str:str):
    new_lines = []
    for line in asn_str.split('\n'):
        if "::= '" in line:
            # fixed_line = line.replace(" ::= ", " ")
            # fixed_line = line.replace(" ::= ", " (").replace("'H", "'H)")
            pass
        else:
            fixed_line = line
        new_lines.append(fixed_line)
    new_asn_str = '\n'.join(new_lines)
    return new_asn_str

def fix_etsi_efc_aso_asn_txt_choices(asn_str:str):
    new_lines = []
    for index, line in enumerate(asn_str.split('\n')):
        if index < 82:
            fixed_line = line
        elif 'CHOICE' in line:
            fixed_line = line.replace('CHOICE', 'INTEGER(0..7)')
        elif "Bit-String-1B ::= " in line:
            fixed_line = line.replace(" Bit-String-1B ::= ", "(").replace("'H", "'H)")
        else:
            fixed_line = line
        new_lines.append(fixed_line)
    new_asn_str = '\n'.join(new_lines)
    return new_asn_str


def fix_etsi_asn_file(asn_filename, fix_choice_defs=False):
    with open(f'ASN/temp/ETSI ES 200 674-3-1 V3.0.0 (2010-06)/{asn_filename}', 'r') as asn_file:
        asn_str = asn_file.read()

    new_asn_str = fix_etsi_asn_txt_sequence_fixed_field_values(asn_str)
    if fix_choice_defs:
        new_asn_str = fix_etsi_efc_aso_asn_txt_choices(asn_str)

    with open(f'ASN/temp/ETSI ES 200 674-3-1 V3.0.0 (2010-06)_fixed/{asn_filename}', 'w') as asn_out_file:
        asn_out_file.write(new_asn_str)

if __name__ == '__main__':
    fix_etsi_asn_file('ETSI-EFC-ACSE_V3.0.0.asn')
    fix_etsi_asn_file('ETSI-EFC-ASO_V3.0.0.asn', fix_choice_defs=True)