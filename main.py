"""main"""
import sys
import re
from late import late_list
from Calculating_the_Number_of_Points import deadline_score
from colorama import Fore, Style, init

init(autoreset = True)

dict_student ={
    "Иванов" : "09-10-2020",
    "Петров" : "11-10-2020"
    }

def enter(text):
    """Ввод значений"""
    while True:
        try:
            print(f"{Style.BRIGHT}{text}")
            action = int(input())
            if action > 0:
                return action
            print(f"{Fore.RED}{Style.BRIGHT}Введите"
                  f" положительное число!")
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Пожалуйста,"
                  f" введите число")

def enter_date(text):
    """Ввод даты сдачи или дэдлайна в формате DD-MM-YYYY"""
    while True:
        try:
            print(f"{Style.BRIGHT}Введите дату в формате DD-MM-YYYY ({text})")
            action = input()
            if len(re.findall("\d\d-\d\d-\d\d\d\d", action)) == 1:
                return action
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Введите"
                  f" дату в указанном формате!")

def convert_date(date):
    data_date = re.split("-", date)
    day = data_date[0]
    month = data_date[1]
    year = data_date[2]
    date_string = year+"-"+month+"-"+day
    return date_string

while True:
    #Интерфейс программы
    function = enter(f"{Fore.CYAN}{Style.BRIGHT}"
                     f"(1 - Рассчёт оценки)\n"
                     f"(2 - Вывести список учеников,"
                     f" сдавших работу после дэдлайна)\n"
                     f"(3 - Выход из программы)")
    if function == 1:
        pass_date = convert_date(enter_date("Дата сдачи работы учеником"))
        deadline_date = convert_date(enter_date("Дата дэдлайна"))
        print(deadline_score(pass_date, deadline_date))
    elif function == 2:
        deadline_date = enter_date("Дата дэдлайна")
        print(late_list(dict_student, deadline_date))
    elif function == 3:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Программа"
              f" завершила выполнение")
        sys.exit()
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Пожалуйста, выберите действие")
