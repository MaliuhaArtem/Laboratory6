import os

class PodorozhiApp:
    def __init__(self):
        self.podorozhi_list = []

    def create_podorozh(self, name, start_date, end_date, destination, budget):
        podorozh = {
            'Name': name,
            'Start Date': start_date,
            'End Date': end_date,
            'Destination': destination,
            'Budget': budget
        }
        self.podorozhi_list.append(podorozh)
        filename = f"{name.replace(' ', '_').lower()}_details.txt"
        self.save_to_file(filename)
        print(f"Подорож створено успішно, дані збережено у файл {filename}!")

    def save_to_file(self, filename):
        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        with open(filename, 'w') as file:
            for podorozh in self.podorozhi_list:
                file.write('\n'.join([f"{key}: {value}" for key, value in podorozh.items()]) + '\n\n')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.podorozhi_list = []
                for line in file:
                    items = line.strip().split(': ')
                    if len(items) == 2:
                        key, value = items
                        podorozh = {key: value}
                        self.podorozhi_list.append(podorozh)
            print(f"Дані завантажено з файлу {filename}")
        except FileNotFoundError:
            print("Файл не знайдено. Створіть новий.")

    def delete_file(self, filename):
        try:
            os.remove(filename)
            print(f"Файл {filename} успішно видалено.")
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")

    def display_file_content(self, filename):
        try:
            with open(filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")

app = PodorozhiApp()

while True:
    print("\n1. Створити нову подорож")
    print("2. Видалити файл")
    print("3. Переглянути файл")
    print("4. Завершити роботу")

    choice = input("Оберіть опцію (1-4): ")

    if choice == '1':
        name = input("Введіть назву подорожі: ")
        start_date = input("Введіть дату початку (формат зручний для вас: ")
        end_date = input("Введіть дату закінчення (формат зручний для вас: ")
        destination = input("Введіть місце призначення: ")
        budget = input("Введіть бюджет: ")
        app.create_podorozh(name, start_date, end_date, destination, budget)

    elif choice == '2':
        filename = input("Введіть ім'я файлу для видалення(в кінці обов'язково .txt): ")
        app.delete_file(filename)

    elif choice == '3':
        filename = input("Введіть ім'я файлу для перегляду(в кінці обов'язково .txt): ")
        app.display_file_content(filename)

    elif choice == '4':
        print("Роботу завершено. Дякую за використання додатку!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
