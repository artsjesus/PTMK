import os
import datetime
import random
import string
import time
from sqlalchemy import Column, Integer, String, Date, Index
from sqlalchemy.orm import sessionmaker, declarative_base
from db_connection import DatabaseManager
from unit import create_employee, show_all_employees, fill_database, search_males_with_f_surname
from employee import Employee


def main():

    db_manager = DatabaseManager()
    db_manager.create_all()

    while True:
        print("\nВыберите действие:")
        print("1 - Создать сотрудника")
        print("2 - Показать всех сотрудников")
        print("3 - Заполнить базу данных 1 миллионом записей")
        print("4 - Поиск мужчин с фамилией, начинающейся на 'F'")
        print("5 - Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            full_name = input("Введите полное имя: ")
            birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
            gender = input("Введите пол (Male/Female): ")
            create_employee(db_manager, full_name, birth_date, gender)
        elif choice == '2':
            show_all_employees(db_manager)
        elif choice == '3':
            fill_database(db_manager)
        elif choice == '4':
            search_males_with_f_surname(db_manager)
        elif choice == '5':
            print("Выход из приложения.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


# Запуск программы
if __name__ == '__main__':
    main()
