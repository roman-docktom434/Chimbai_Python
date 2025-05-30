'''
В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
(например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
количество полученных элементов.
'''
import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'\b\d{4}\s*(?:год|года|году)\b'

years = re.findall(pattern, text, flags=re.IGNORECASE)

print("Найденные вхождения лет деятельности писателя:")
for y in years:
    print(y)
print(f"\nВсего найдено элементов: {len(years)}")