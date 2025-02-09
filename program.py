import json
import os

DB_FILE = "database.json"  # Имя файла для хранения данных

# Проверка существования файла. В случае отсутствия создается пустая база
if not os.path.isfile(DB_FILE):
    with open(DB_FILE, "w") as file:
        file.write("[]") # Внутри будут сами данные

# Загрузка данные из файла базы данных
def load_data():
    with open(DB_FILE, "r") as file:
        return json.load(file)

# Сохранение данных обратно в файл базы данных
def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4) # Сама запись данных (сохраняется построчно)

# Вывод всех записей в базе данных
def list_records():
    data = load_data()
    if not data:
        print("Записей нет.")
    else:
        for i, record in enumerate(data):
            print(f"{i + 1}. {record}")

# Добавление новой записи в базу данных, не стирая пробелы в тексте, кроме начала и конца
def add_record():
    record = input("Введите запись: ").strip()
    if record:
        data = load_data() # Загрузка данных из БД
        data.append(record) # Добавление информации
        save_data(data) # Сохранение изменений данных в файле
        print("Запись добавлена.")
    else:
        print("Запись не может быть пустой.")

# Удаление записи по её номеру
def delete_record():
    data = load_data()
    if not data: # Проверка наличия информации
        print("База данных пуста. Добавьте запись сначала.")
        return

    list_records() # Вывод информации
    num = input("Введите номер записи для удаления: ").strip() # Выбор удаления записи
    # Проверка строки, состоит ли она только из цифр или содержит символы.
    if num.isdigit() and 1 <= int(num) <= len(data): # В целом для предотвращения ошибок
        removed = data.pop(int(num) - 1) # Удаление конкретной строки
        save_data(data)
        print(f"Запись '{removed}' удалена.")
    else:
        print("Некорректный номер записи.")

# Редактирование существующую запись по номеру
def edit_record():
    data = load_data()
    if not data: 
        print("База данных пуста. Добавьте запись сначала.")
        return

    list_records() 
    num = input("Введите номер записи для редактирования: ").strip()
    if num.isdigit() and 1 <= int(num) <= len(data):
        new_content = input("Введите новый текст: ").strip()
        if new_content: # Проверка наличия нового текста
            data[int(num) - 1] = new_content # Замена информации
            save_data(data)
            print("Запись обновлена.")
        else:
            print("Текст не может быть пустым.")
    else:
        print("Некорректный номер записи.")

# Главное меню программы
def main():
    while True:
        print("\n--- Меню ---")
        print("1 - Просмотреть записи")
        print("2 - Добавить запись")
        print("3 - Удалить запись")
        print("4 - Редактировать запись")
        print("5 - Выход")

        choice = input("Ваш выбор: ").strip() # Удаление пробелов / "проверка" на дурака

        if choice == "1":
            list_records()
        elif choice == "2":
            add_record()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            edit_record()
        elif choice == "5":
            print("Выход.")
            break
        else:
            print("Некорректный ввод. Попробуйте ещё раз.")


# Запуск меню (запуск отдельной функции)
if __name__ == "__main__":
    main()
