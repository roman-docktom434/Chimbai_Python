def lower_gen(text):
    # Для каждого символа возвращаем его нижний регистр, если это буква, иначе — символ без изменений
    for char in text:
        yield char.lower() if char.isalpha() else char

# Пример использования:
input_text = input('Введите текст: ')
result = ''.join(lower_gen(input_text))
print(result)  # Выведет: hello, world! 123
