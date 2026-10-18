def parse_event(line: str) -> dict:
    clean_line = line.strip()

    if not clean_line:
        return {"time": "", "level": "EMPTY", "message": ""}

    parts = clean_line.split(maxsplit=2)

    if len(parts) < 3:
        raise ValueError("Неверный формат")

    time_str, level, message = parts

    if level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError("Неизвестный уровень")

    return {
        "time": time_str,
        "level": level,
        "message": message
    }


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        try:
            event = parse_event(line)
            level = event["level"]
            if level == "EMPTY":
                continue

        except ValueError:
            level = "BROKEN"

        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue

    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу\n"]

    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")

    lines.append("\nЧастые ошибки:")

    if not errors:
        lines.append("- Нет ошибок")
    else:
        for msg, count in errors:
            lines.append(f"- {msg} — {count}")

    return "\n".join(lines) + "\n"







