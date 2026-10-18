import sys
from logstats import parse_event, count_levels, top_errors, format_report


def main():
    filename = input("Введите имя файла: ").strip()

    total_lines = 0
    total_errors = 0
    total_broken = 0

    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue

                total_lines += 1

                try:
                    event = parse_event(line)
                    if event["level"] == "ERROR":
                        total_errors += 1
                except ValueError:
                    total_broken += 1

    except FileNotFoundError:
        print("Файл не найден!")
        return

    print(total_lines)
    print(total_errors)
    print(total_broken)

    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    counts = count_levels(lines)
    errors = top_errors(lines, 3)

    report_text = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as f_out:
        f_out.write(report_text)


if __name__ == "__main__":
    main()




