"""
Задание 7:
Создание базового класса "Транспортное средство" и его наследование для создания
классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
общие свойства, такие как максимальная скорость и количество колес, а классы-
наследники будут иметь свои уникальные свойства и методы.
"""

class Vehicle:
    def __init__(self, max_speed, wheels_count):
        self.max_speed = max_speed
        self.wheels_count = wheels_count

    def get_info(self):
        return f"Максимальная скорость: {self.max_speed} км/ч\nКоличество колес: {self.wheels_count}"


class Car(Vehicle):
    def __init__(self, max_speed, wheels_count, body_type, doors_count):
        super().__init__(max_speed, wheels_count)
        self.body_type = body_type
        self.doors_count = doors_count

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}\nТип кузова: {self.body_type}\nКоличество дверей: {self.doors_count}"


class Motorcycle(Vehicle):
    def __init__(self, max_speed, wheels_count, moto_type, engine_volume):
        super().__init__(max_speed, wheels_count)
        self.moto_type = moto_type
        self.engine_volume = engine_volume

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}\nТип мотоцикла: {self.moto_type}\nОбъем двигателя: {self.engine_volume} куб.см"


if __name__ == "__main__":
    car = Car(220, 4, "Седан", 4)
    motorcycle = Motorcycle(280, 2, "Спортивный", 1000)

    print("Информация об автомобиле:")
    print(car.get_info())
    print("\nИнформация о мотоцикле:")
    print(motorcycle.get_info()) 