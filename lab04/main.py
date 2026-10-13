import sys
from stats import parse_record, read_valid, average_by_city, warmest_city


def main():
    # Читаем весь ввод
    lines = sys.stdin.read().splitlines()

    total_lines = len(lines)
    valid_records = read_valid(lines)
    parsed_count = len(valid_records)

    # Количество пропущенных строк из-за ошибок.
    # Считаем так: общее кол-во минус успешно разобранные.
    # Это автоматически исключает пустые строки, так как они не считаются ошибками,
    # но и не попадают в valid_records.
    skipped_count = total_lines - parsed_count

    if parsed_count == 0:
        # Обработка случая, когда нет валидных данных
        print(parsed_count)
        print(skipped_count)
        print("0.0")
        return

    warmest = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    avg_temp = averages.get(warmest, 0.0)

    # Вывод строго по заданию
    print(parsed_count)
    print(skipped_count)
    # Вывод средней температуры с одним знаком после запятой
    print(f"{avg_temp:.1f}")


if __name__ == "__main__":
    main()



