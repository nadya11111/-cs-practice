def parse_event(line: str) -> dict:


    parts = line.strip().split(maxsplit=2)


    if len(parts) < 3:
        raise ValueError("Недостаточно данных в строке")

    time, level, message = parts


    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError("Неизвестный уровень лога")

    return {
        "time": time,
        "level": level,
        "message": message
    }


def count_levels(lines) -> dict:

    counts = {}
    for line in lines:

        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:

            level = "BROKEN"

        counts[level] = counts.get(level, 0) + 1

    return counts


def top_errors(lines, n: int) -> list[list]:

    error_counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:

            continue


    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))

    result = [[msg, count] for msg, count in sorted_errors[:n]]
    return result


def format_report(counts: dict, errors: list[list]) -> str:

    report_lines = ["Отчёт по журналу\n"]


    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")

    report_lines.append("\nЧастые ошибки:")

    if not errors:
        report_lines.append("- Нет ошибок")
    else:
        for msg, count in errors:
            report_lines.append(f"- {msg} — {count}")

    return "\n".join(report_lines)





