def parse_record(line: str) -> dict:
    """
    Разбирает одну строку журнала в словарь.
    Формат строки: 'город;температура;дата'

    Если строка некорректна — вызывает ValueError.
    """
    # 1. Разделяем строку по точке с запятой
    parts = line.split(";")

    # 2. Проверяем, что получилось ровно 3 части
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}")

    city, temp_str, date = parts

    # 3. Проверяем, что город и дата не пустые
    if not city.strip():
        raise ValueError("Название города пустое")
    if not date.strip():
        raise ValueError("Дата пустая")

    # 4. Пробуем преобразовать температуру в число
    try:
        temp = float(temp_str)
    except ValueError:
        # Если не получилось — возбуждаем свою ошибку с понятным текстом
        raise ValueError(f"Температура '{temp_str}' не является числом")

    # 5. Возвращаем словарь с данными
    return {
        "city": city.strip(),
        "temp": temp,
        "date": date.strip()
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
    """
    Считает среднюю температуру по каждому городу.
    Возвращает словарь: {'Город': средняя_температура}
    """
    # Словари для накопления суммы температур и количества записей
    total_temp = {}
    count_records = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temp"]

        # Накапливаем сумму
        total_temp[city] = total_temp.get(city, 0.0) + temp
        # Накапливаем количество
        count_records[city] = count_records.get(city, 0) + 1

    # Считаем среднее и округляем до десятых
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