import json


def csv_to_records(text):
    lines = text.strip().split('\n')
    if len(lines) == 0:
        return []

    h = lines[0].split(',')
    hdr = [x.strip() for x in h]
    res = []

    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "":
            continue

        vals = line.split(',')
        d = {}
        for j in range(len(hdr)):
            v = vals[j].strip() if j < len(vals) else ""
            d[hdr[j]] = v
        res.append(d)
    return res


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


def merge_by_key(rows, extra, key):
    res = []
    for row in rows:
        k_val = row[key]
        m = {}
        if k_val in extra:
            m.update(extra[k_val])
        m.update(row)
        res.append(m)
    return res


def records_to_json(records):
    return json.dumps(records, indent=2, ensure_ascii=False, sort_keys=True)