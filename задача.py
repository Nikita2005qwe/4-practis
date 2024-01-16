from datetime import date

def delta_day(first_date, second_date):
    """Вывести число дней между днями"""
    first_date = date.fromisoformat(first_date)
    second_date = date.fromisoformat(second_date)
    return abs(first_date - second_date).days
