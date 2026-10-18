import sys
from logstats import parse_event, count_levels, top_errors, format_report


def main():

    filename = input("Введите имя файла: ").strip()

    total_parsed = 0
    total_errors = 0
    total_broken = 0


    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    event = parse_event(line)
                    total_parsed += 1
                    if event["level"] == "ERROR":
                        total_errors += 1
                except ValueError:
                    total_broken += 1
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        sys.exit(1)


    print(total_parsed)
    print(total_errors)
    print(total_broken)


    with open(filename, encoding="utf-8") as f:
        counts = count_levels(f)

    with open(filename, encoding="utf-8") as f:
        errors = top_errors(f, 3)

    report_text = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as f_out:
        f_out.write(report_text)


if __name__ == "__main__":
    main()





