def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}")

    city, temp_str, date = parts

    # Очищаем ВСЕ поля от пробелов
    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()

    if not city:
        raise ValueError("Название города пустое")
    if not date:
        raise ValueError("Дата пустая")

    # Заменяем запятую на точку (для чисел вида -3,5)
    temp_str = temp_str.replace(",", ".")

    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }


def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    valid_records = []
    error_count = 0

    for line in lines:
        if not line.strip():
            continue  # пустые строки пропускаем, но НЕ считаем ошибками
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            error_count += 1  # считаем только реальные ошибки

    return valid_records, error_count


def average_by_city(records: list[dict]) -> dict:
    total_temp = {}
    count_records = {}
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]  # Изменено на "temperature"
        total_temp[city] = total_temp.get(city, 0.0) + temp
        count_records[city] = count_records.get(city, 0) + 1

    averages = {}
    for city in total_temp:
        avg = total_temp[city] / count_records[city]
        averages[city] = round(avg, 1)
    return averages


def warmest_city(records: list[dict]) -> str:
    """
    Возвращает название самого тёплого города.
    При равенстве средних температур — первый по алфавиту.
    """
    if not records:
        return ""

    # Получаем средние температуры по городам
    averages = average_by_city(records)

    if not averages:
        return ""

    # Сортируем города:
    # 1) по средней температуре (по убыванию, поэтому минус)
    # 2) при равенстве — по алфавиту (по возрастанию)
    sorted_cities = sorted(
        averages.keys(),
        key=lambda city: (-averages[city], city)
    )

    return sorted_cities[0]