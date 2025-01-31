'''
Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
отражающая продажи продукции по дням в кг. Преобразовать информацию из
строки в словари, с использованием функции найти минимальные продажи по
каждому виду продукции, результаты вывести на экран
'''
def parse_sales(data):
    parts = data.split()
    products = {}
    current_product = None
    current_sales = []
    for item in parts:
        if item.isalpha():
            if current_product:
                products[current_product] = current_sales
            current_product = item
            current_sales = []
        else:
            current_sales.append(int(item))
    if current_product:
        products[current_product] = current_sales
    return products


def find_min_sales(products):
    min_sales = {product: min(sales) for product, sales in products.items()}
    return min_sales


data = "груши 45 991 63 100 12 морковь 13 47 26 0 16"

sales_data = parse_sales(data)
min_sales = find_min_sales(sales_data)
for product, min_value in min_sales.items():
    print(f"Минимальные продажи для {product}: {min_value} кг")