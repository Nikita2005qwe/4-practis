"""Вычисление оценки"""
from datetime import date

def delta_day(first_date, second_date):
    """
    Вывести число дней между днями.
    first_date - дата сдачи
    second_date -дата дэдлайна
    """
    first_date = date.fromisoformat(first_date)
    second_date = date.fromisoformat(second_date)
    return (first_date - second_date).days

def output_weeks(days):
    """
    Вывести число недель пройденое после дедлайна.
    Возвращает отрицательное число, если дедлайн не наступил,
    а работа была сдана.
    """
    if days > 0:
        return days//7
    else:
        return -1

def output_assessment(num_weeks):
    """
    Выводит оценку ученика в зависимости от недель до
    сдачи работы, пройденных после дедлайна
    """
    if num_weeks == -1:
        return 5
    if 0 <= num_weeks < 4:
        return 5 - num_weeks - 1
    if num_weeks >= 4:
        return 0