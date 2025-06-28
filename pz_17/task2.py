'''
Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
нечетные числа в порядке возрастания их индексов, а также их количество K.
'''
import tkinter as tk
from tkinter import ttk, messagebox

class NumberAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализатор чисел")
        self.root.geometry("400x600")
        
        # Создаем и настраиваем основной контейнер
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Создаем поля ввода
        self.entries = []
        for i in range(10):
            ttk.Label(main_frame, text=f"Число {i + 1}:").grid(row=i, column=0, padx=5, pady=2)
            entry = ttk.Entry(main_frame, width=20)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries.append(entry)
        
        # Кнопка анализа
        ttk.Button(main_frame, text="Анализировать", command=self.analyze_numbers).grid(row=10, column=0, columnspan=2, pady=10)
        
        # Область для вывода результатов
        self.result_text = tk.Text(main_frame, height=5, width=40)
        self.result_text.grid(row=11, column=0, columnspan=2, pady=10)
        
    def analyze_numbers(self):
        numbers = []
        
        # Проверка и сбор введенных чисел
        for i, entry in enumerate(self.entries):
            try:
                num = int(entry.get())
                numbers.append(num)
            except ValueError:
                messagebox.showerror("Ошибка", f"Пожалуйста, введите корректное целое число в поле {i + 1}")
                return
        
        # Находим нечетные числа
        odd_numbers = [num for num in numbers if num % 2 != 0]
        
        # Формируем результат
        result = "Нечетные числа в порядке возрастания их индексов:\n"
        result += " ".join(map(str, odd_numbers))
        result += f"\n\nКоличество нечетных чисел: {len(odd_numbers)}"
        
        # Очищаем и выводим результат
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberAnalyzer(root)
    root.mainloop()