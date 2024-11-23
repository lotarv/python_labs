class InvalidArgumentError(Exception):
    """
    Исключение для некорректного аргумента.
    """
    pass

def is_html_image_tag(input_string):

    if not isinstance(input_string, str):
        return False

    input_string = input_string.strip()
    return input_string.startswith('<img') and input_string.endswith('>') and 'src=' in input_string

def validate_html_image_tag(input_string):
    if not is_html_image_tag(input_string):
        raise InvalidArgumentError("Некорректный аргумент: строка не является HTML-кодом изображения.")
    return input_string


try:
    html_code = "<img src=\"image.jpg\" alt=\"Description\">"
    if is_html_image_tag(html_code):
        print("Корректный HTML-код изображения.")
    else:
        print("Некорректный HTML-код изображения.")

    validated_code = validate_html_image_tag(html_code)
    print("Проверенный HTML-код изображения:", validated_code)
except InvalidArgumentError as e:
    print(e)


try:
    html_code = "<image src=\"image.jpg\" alt=\"Description\">"
    if is_html_image_tag(html_code):
        print("Корректный HTML-код изображения.")
    else:
        print("Некорректный HTML-код изображения.")

    validated_code = validate_html_image_tag(html_code)
    print("Проверенный HTML-код изображения:", validated_code)
except InvalidArgumentError as e:
    print(e)
