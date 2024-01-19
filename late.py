from Calculating_the_Number_of_Points import output_assessment, output_weeks, delta_day
import re

def convert_date(date):
    data_date = re.split("-", date)
    day = data_date[0]
    month = data_date[1]
    year = data_date[2]
    date_string = year+"-"+month+"-"+day
    return date_string

def late_list(dict_student, deadline_date):
    """Функция возвращает список из фамилий людей не успевших сдать работы
    до дэдлайна"""
    list_late_student = []
    for name in dict_student:
        if output_assessment(output_weeks(delta_day(
                convert_date(dict_student[name]),
                convert_date(deadline_date)))) != 5:
            list_late_student.append(name)
    return list_late_student
