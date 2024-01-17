"""main"""
import sys
from colorama import Fore, Style, init

init(autoreset = True)

def enter(text):
    """Ввод значений"""
    while True:
        try:
            print(f"{Style.BRIGHT}{text}")
            action = int(input())
            if action > 0:
                return action
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Введите"
                      f" положительное число!")
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Пожалуйста,"
                  f" введите число")


while True:
    function = enter(f"{Fore.CYAN}{Style.BRIGHT}"
                     f"(1 - Рассчёт оценки)\n"
                     f"(2 - Вывести список учеников,"
                     f" сдавших работу после дэдлайна)")
    if function == 1:
        pass
    elif function == 2:
        pass
    elif function == 3:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Программа"
              f" завершила выполнение")
        sys.exit()
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Пожалуйста, выберите действие")
