"""
Приложение АПТЕКА для автоматизации работы аптечных пунктов. Таблица
Лекарственные Средства должна содержать следующую информацию: Код, Название
препарата, Применение, Количество, Цена, Страна-производитель.
"""

import sqlite3
from sqlite3 import Error, IntegrityError

DB_FILE = "apteka.db"

def create_connection(db_file: str):
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to SQLite (library) — version", sqlite3.sqlite_version)
        return conn
    except Error as e:
        print(f" Ошибка подключения к БД: {e}")
        return None

def create_table(conn: sqlite3.Connection):
    sql = """
    CREATE TABLE IF NOT EXISTS medicines (
        code     INTEGER PRIMARY KEY,
        name     TEXT NOT NULL,
        usage    TEXT,
        quantity INTEGER,
        price    REAL,
        country  TEXT
    );
    """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Таблица medicines готова.")
    except Error as e:
        print(f" Ошибка при создании таблицы: {e}")

def add_medicine(conn: sqlite3.Connection, med: tuple):
    sql = """
    INSERT INTO medicines(code, name, usage, quantity, price, country)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, med)
        conn.commit()
        print(f" Добавлен препарат: {med}")
    except IntegrityError:
        print(f" Препарат с кодом {med[0]} уже существует. Пропуск.")
    except Error as e:
        print(f" Ошибка при вставке препарата: {e}")

def update_medicine(conn: sqlite3.Connection, code: int, updates: dict):
    sql = "UPDATE medicines SET {} WHERE code = ?".format(
        ", ".join(f"{key} = ?" for key in updates.keys())
    )
    try:
        cur = conn.cursor()
        cur.execute(sql, (*updates.values(), code))
        conn.commit()
        print(f" Обновлён препарат с code={code}.")
    except Error as e:
        print(f" Ошибка при обновлении препарата: {e}")

def delete_medicine(conn: sqlite3.Connection, code: int):
    sql = "DELETE FROM medicines WHERE code = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (code,))
        conn.commit()
        print(f" Удалён препарат с code={code}.")
    except Error as e:
        print(f" Ошибка при удалении препарата: {e}")

def display_table(conn: sqlite3.Connection, message: str):
    print(f"\n{message}")
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM medicines;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"❗ Ошибка при чтении таблицы: {e}")

def main():
    conn = create_connection(DB_FILE)
    if conn is None:
        return

    create_table(conn)

    add_medicine(conn, (1, "Парацетамол", "Жаропонижающее", 100, 50.0, "Россия"))
    add_medicine(conn, (2, "Ибупрофен", "Противовоспалительное", 80, 70.0, "Германия"))
    add_medicine(conn, (3, "Аспирин", "Анальгетик", 60, 30.0, "Россия"))
    add_medicine(conn, (4, "Цитрамон", "Анальгетик", 120, 40.0, "Беларусь"))

    display_table(conn, "Состояние таблицы после добавления 4 препаратов:")

    update_medicine(conn, 1, {"quantity": 150, "price": 55.0})
    update_medicine(conn, 2, {"usage": "Болеутоляющее", "quantity": 90})
    update_medicine(conn, 3, {"country": "Китай", "price": 35.0})
    update_medicine(conn, 4, {"name": "Цитрамон П", "quantity": 110})

    display_table(conn, "Состояние таблицы после обновлений:")

    delete_medicine(conn, 1)
    delete_medicine(conn, 2)
    delete_medicine(conn, 4)

    display_table(conn, "Состояние таблицы после удаления 3 препаратов:")

    conn.close()

if __name__ == "__main__":
    main()