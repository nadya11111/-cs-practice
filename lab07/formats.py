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
    def cast(x):
        x = x.strip()

        if x.lower() in ("true", "yes"):
            return True
        if x.lower() in ("false", "no"):
            return False

        try:
            return int(x)
        except ValueError:
            pass

        try:
            x = x.replace(',', '.')
            return float(x)
        except ValueError:
            pass

        return x

    res = {}
    lst_key = ""

    for line in lines:
        if '#' in line:
            line = line[:line.find('#')]

        line = line.strip()
        if line == "":
            continue

        if line.startswith("- "):
            item = line[2:]
            v = cast(item)
            if lst_key != "":
                res[lst_key].append(v)

        elif ":" in line:
            p = line.split(":", 1)
            k = p[0].strip()
            v_str = p[1].strip()

            if v_str == "":
                lst_key = k
                res[k] = []
            else:
                res[k] = cast(v_str)
                lst_key = ""

    return res

def records_to_json(records):
    json_string = json.dumps(records, indent=2, ensure_ascii=False, sort_keys=True)
    return json_string

