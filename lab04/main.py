import sys
from stats import parse_record, read_valid, average_by_city, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    valid_records, error_count = read_valid(lines)
    parsed_count = len(valid_records)

    if parsed_count == 0:
        print(parsed_count)
        print(error_count)
        print("0.0")
        return

    warmest = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    avg_temp = averages[warmest]

    print(parsed_count)
    print(error_count)  # именно количество ошибок, а не разница
    print(f"{avg_temp:.1f}")


if __name__ == "__main__":
    main()
