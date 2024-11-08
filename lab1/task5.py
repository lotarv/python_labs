import re

def find_dates(string):
    # Шаблон для поиска дат в нужном формате
    pattern = r'\b\d{1,2} (?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) \d{4}\b'
    dates = re.findall(pattern, string)
    return dates

# Пример строки
string = "События происходили 31 декабря 2022, а также 15 мая 2023 и 1 января 2021."

# Поиск всех дат
found_dates = find_dates(string)
print("Найденные даты:", found_dates)
