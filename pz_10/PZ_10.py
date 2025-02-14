# Туристические агентства и их туры
voyage = ['Мексика', 'Канада', 'Израиль', 'Италия', 'США']
reina_tour = ['Англия', 'Япония', 'Канада', 'ЮАР']
raduga = ['США', 'Испания', 'Швеция', 'Австралия']

# Проверка, в каких турагентствах есть туры в Канаду
canada_agencies = []
if 'Канада' in voyage:
    canada_agencies.append('Вояж')
if 'Канада' in reina_tour:
    canada_agencies.append('РейнаТур')
if 'Канада' in raduga:
    canada_agencies.append('Радуга')

# Проверка, в каких турагентствах есть туры в США
usa_agencies = []
if 'США' in voyage:
    usa_agencies.append('Вояж')
if 'США' in reina_tour:
    usa_agencies.append('РейнаТур')
if 'США' in raduga:
    usa_agencies.append('Радуга')

# Вывод результатов
print("Туры в Канаду предлагаются в агентствах:", ', '.join(canada_agencies))
print("Туры в США предлагаются в агентствах:", ', '.join(usa_agencies))
