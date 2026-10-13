def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}")

    city, temp_str, date = parts

    # Применяем strip() ко всем полям, включая температуру
    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()

    if not city:
        raise ValueError("Название города пустое")
    if not date:
        raise ValueError("Дата пустая")

    try:
        # Теперь temp_str без пробелов, float сработает корректно
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом")

    return {
        "city": city,
        "temperature": temperature,  # Изменено на "temperature"
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    """
    Принимает список строк, возвращает список словарей с валидными записями.
    Пустые строки и строки с ошибками пропускаются.
    """
    valid_records = []

    for line in lines:
        # Пропускаем пустые строки молча (не считаем их ошибкой)
        if not line.strip():
            continue

        # Пытаемся разобрать строку
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Если строка негодная — просто пропускаем её
            continue

    return valid_records


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