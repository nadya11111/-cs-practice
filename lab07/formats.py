import json


def csv_to_records(text):
    lines = text.strip().split('\n')
    if len(lines) == 0:
        return []

    headers_line = lines[0]
    headers = headers_line.split(',')

    clean_headers = []
    for h in headers:
        clean_headers.append(h.strip())

    records = []

    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == '':
            continue


        values = line.split(',')

        record = {}

        for j in range(len(clean_headers)):
            if j < len(values):
                val = values[j].strip()
            else:
                val = ""
            header_name = clean_headers[j]
            record[header_name] = val
        records.append(record)
    return records


