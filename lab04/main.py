import sys
from stats import parse_record, read_valid, average_by_city, warmest_city


def main():
    lines = sys.stdin.read().splitlines()

    # Считаем непустые строки
    non_empty_lines = [line for line in lines if line.strip()]

    # Получаем список валидных записей (только список!)
    valid_records = read_valid(lines)
    parsed_count = len(valid_records)

    # Считаем ошибки как разницу
    skipped_count = len(non_empty_lines) - parsed_count

    if parsed_count == 0:
        print(parsed_count)
        print(skipped_count)
        print("0.0")
        return

    warmest = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    avg_temp = averages[warmest]

    print(parsed_count)
    print(skipped_count)
    print(f"{avg_temp:.1f}")


if __name__ == "__main__":
    main()






