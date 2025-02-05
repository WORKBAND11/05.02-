import pandas as pd

def main():
    # Загрузка данных из Excel файла
    file_path = input("Введите путь к вашему Excel файлу (например, 'marks.xlsx'): ")
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return

    while True:
        print("\nВыберите опцию:")
        print("1. Вывести все данные из таблицы")
        print("2. Вывести строку или столбец")
        print("3. Вывести конкретную ячейку")
        print("4. Вычесть среднее арифметическое из строки или столбца")
        print("0. Выход")

        choice = input("Введите номер опции: ")

        if choice == '1':
            print("\nВсе данные из таблицы:")
            print(df)

        elif choice == '2':
            print("\nВведите 'row' для строки или 'column' для столбца:")
            axis_choice = input("Ваш выбор: ").strip().lower()

            if axis_choice == 'row':
                row_index = int(input("Введите номер строки (начиная с 0): "))
                if 0 <= row_index < len(df):
                    print(f"\nДанные строки {row_index}:")
                    print(df.iloc[row_index])
                else:
                    print("Неверный номер строки.")

            elif axis_choice == 'column':
                col_index = input("Введите название столбца: ")
                if col_index in df.columns:
                    print(f"\nДанные столбца '{col_index}':")
                    print(df[col_index])
                else:
                    print("Неверное название столбца.")
            else:
                print("Неверный выбор. Пожалуйста, введите 'row' или 'column'.")

        elif choice == '3':
            row_index = int(input("Введите номер строки (начиная с 0): "))
            col_index = input("Введите название столбца: ")
            if 0 <= row_index < len(df) and col_index in df.columns:
                print(f"\nДанные ячейки ({row_index}, '{col_index}'): {df.at[row_index, col_index]}")
            else:
                print("Неверные координаты ячейки.")

        elif choice == '4':
            print("\nВведите 'row' для строки или 'column' для столбца:")
            axis_choice = input("Ваш выбор: ").strip().lower()

            if axis_choice == 'row':
                row_index = int(input("Введите номер строки (начиная с 0): "))
                if 0 <= row_index < len(df):
                    row_data = df.iloc[row_index]
                    row_data_numeric = pd.to_numeric(row_data, errors='coerce')
                    mean_value = row_data_numeric.mean()
                    print(f"\nСреднее арифметическое строки {row_index}: {mean_value}")
                else:
                    print("Неверный номер строки.")

            elif axis_choice == 'column':
                col_index = input("Введите название столбца: ")
                if col_index in df.columns:
                    col_data = df[col_index]
                    col_data_numeric = pd.to_numeric(col_data, errors='coerce')
                    mean_value = col_data_numeric.mean()
                    print(f"\nСреднее арифметическое столбца '{col_index}': {mean_value}")
                    print(f"Результат вычитания среднего арифметического из столбца '{col_index}':")
                    print(col_data_numeric - mean_value)
                else:
                    print("Неверное название столбца.")
            else:
                print("Неверный выбор. Пожалуйста, введите 'row' или 'column'.")

        elif choice == '0':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()