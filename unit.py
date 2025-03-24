import datetime
import random
import string
import time
from employee import Employee


def create_employee(db_manager, full_name, birth_date, gender):
    birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()
    employee = Employee(full_name=full_name, birth_date=birth_date, gender=gender)
    db_manager.add_employee(employee)
    print(f"Сотрудник {full_name} добавлен.")


# Функция для вывода всех сотрудников
def show_all_employees(db_manager):
    employees = db_manager.get_all_employees()
    for employee in employees:
        print(f"{employee.full_name}, {employee.birth_date}, {employee.gender}, {employee.age()} лет")


# Функция для заполнения базы данных случайными данными
def fill_database(db_manager):
    def generate_name():
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(5)) + " " + ''.join(
            random.choice(string.ascii_uppercase) for _ in range(5)) + " " + ''.join(
            random.choice(string.ascii_uppercase) for _ in range(5))

    def generate_employee():
        return Employee(
            full_name=generate_name(),
            birth_date=datetime.date(random.randint(1970, 2000), random.randint(1, 12), random.randint(1, 28)),
            gender=random.choice(["Male", "Female"])
        )

    employees = [generate_employee() for _ in range(1000000)]

    # Добавление 100 записей с фамилией на "F" и полом "Male"
    for _ in range(100):
        full_name = "F" + ''.join(random.choice(string.ascii_uppercase) for _ in range(4)) + " " + ''.join(
            random.choice(string.ascii_uppercase) for _ in range(5)) + " " + ''.join(
            random.choice(string.ascii_uppercase) for _ in range(5))
        employees.append(Employee(full_name=full_name,
                                  birth_date=datetime.date(random.randint(1970, 2000), random.randint(1, 12), random.randint(1, 28)),
                                  gender="Male"))

    db_manager.bulk_add(employees)
    print("База данных заполнена 1 миллионом записей, включая 100 записей с фамилией на 'F' и полом 'Male'.")


# Функция для поиска сотрудников с мужским полом и фамилией на букву "F"
def search_males_with_f_surname(db_manager):
    start_time = time.time()

    # Фильтр для поиска сотрудников с мужским полом и фамилией на букву "F"
    result = db_manager.search_employees(Employee.gender == "Male", Employee.full_name.like("F%"))

    end_time = time.time()
    execution_time = end_time - start_time

    for employee in result:
        print(f"{employee.full_name}, {employee.birth_date}, {employee.gender}, {employee.age()} лет")

    print(f"Время выполнения запроса: {execution_time:.4f} секунд")

    return execution_time
