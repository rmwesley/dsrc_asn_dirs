asn_filename = 'EFC-ACSE_V3.0.0.asn'
asn_filename = 'EFC-ASO_V3.0.0.asn'

with open(f'ASN/temp/ETSI ES 200 674-3-1 V3.0.0 (2010-06)/{asn_filename}', 'r') as asn_file:
    asn_str = asn_file.read()

new_lines = []
for line in asn_str.split('\n'):
    if "INTEGER ::= " in line:
        fixed_line = line.replace(" INTEGER ::= ", " ::=")
    elif "::= '" in line:
        fixed_line = line.replace(" ::= '", " ('").replace("'H", "'H)")
    else:
        fixed_line = line
    new_lines.append(fixed_line)

with open(f'ASN/temp/ETSI ES 200 674-3-1 V3.0.0 (2010-06)_fixed/{asn_filename}', 'w') as asn_out_file:
    asn_out_file.write('\n'.join(new_lines))