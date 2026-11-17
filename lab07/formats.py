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


def merge_by_key(rows, extra, key):
    new_rows = []

    for row in rows:
        my_key_val = row[key]

        merged_record = {}

        if my_key_val in extra:
            extra_data = extra[my_key_val]
            for k in extra_data:
                merged_record[k] = extra_data[k]

        for k in row:
            merged_record[k] = row[k]
        new_rows.append(merged_record)
    return new_rows


def parse_settings(lines):
    def convert_value(text_val):
        text_val = text_val.strip()
        if text_val.lower() == "true" or text_val.lower() == "yes":
            return True
        if text_val.lower() == "false" or text_val.lower() == "no":
            return False
        try:
            return int(text_val)
        except ValueError:
            pass
        try:
            text_val = text_val/replace(',','.')
            return float(text_val)
        except ValueError:
            pass
        return text_val

    result = {}
    current_list_name = ""
    for line in lines:
        if '#' in line:
            hash_index = line.find('#')
            line = line[:hash_index]

        line = line.strip()
        if line == "":
            continue
        if line.startswith("- "):
            item_text = line[2:]
            converted_item = convert_value(item_text)

            if current_list_name != "":
                result[current_list_name].append(converted_item)

        elif ":" in line:
            parts = line.split(":", 1)
            key = parts[0].strip()
            val_str = parts[1].strip()

            if val_str == "":
                current_list_name = key
                result[key] = []
            else:
                result[key] = convert_value(val_str)
                current_list_name = ""
    return result


def records_to_json(records):
    json_string = json.dumps(records, indent=2, ensure_ascii=False, sort_keys=True)
    return json_string

