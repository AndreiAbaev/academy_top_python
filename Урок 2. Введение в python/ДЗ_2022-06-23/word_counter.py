with open('war and peace.txt', encoding='utf-8') as f:
    # Считываем текст.
    text = f.read()

    # Приводим к нижнему регистру.
    text = text.lower()

    # Создаем множество символов из текста.
    text_set = set(text)

    # Создаем множество допустимых символов (символы кириллицы, пробел и символ новой строки).
    valid_char = set([chr(i) for i in range(ord('А'), ord('я') + 1)] + ['Ё', 'ё', ' ', '\n'])

    # Создаем множество недопустимых символов (вычитаем из множества символов текста множество допустимых символов).
    invalid_char = text_set.difference(valid_char)

    # Удаляем каждый недопустимый символ из текста.
    for ch in invalid_char:
        text = text.replace(ch, '')

    # Разделяем текст на слова.
    text = text.split()

    # Создаем словарь, где ключ - слово, значение - частота слова в тексте.
    frequency = {}

    for word in text:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1


# Запись результата в текстовый файл.
with open('result.txt', 'w') as new_f:
    for word, freq in frequency.items():
        if freq % 10 in (2, 3, 4):
            new_f.write(f'Слово {word} встречается {freq} раза\n')
        else:
            new_f.write(f'Слово {word} встречается {freq} раз\n')


