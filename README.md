Это программа которая вычислит какую оценку поставить ученику если он выполнил работу на отлично но не уложился или наоборот уложился в дэдлайн

Первая функция принимает на вход два параметра в формате DD-MM-YYYY, чтобы выяснить сколько дней между данными датами прошло и в случае если число отрицательное и работа была сдана в срок
поставить оценку отлично, а во всех остальных случаях вычитать из оценки число недель пройденных после дэдлайна.

Код разбит на модули что позволяет его быстро прочитать

1 модуль (main)
реализован консольный интерфэйс связанный с зацикливанием программы
также дополнительно введены функции ввода значений типа натуральное число и дат
добавленна функция перевода даты в формат обработки
Формат обработки YYYY-MM-DD удобный формат с которам работает библеотека datetime

2 модуль (late)
в данном модуле размещена функция, которая принимает на вход словарь из фамилий и соответствующих дат сдачи проектов
функция сравнивает на каждой итерации дату сдачи и дату дэдлайна, которая передаётся как второй параметр в функцию
и в случае, если работа сдана после дэдлайна добавляет фамилию в список list_late_student и в конце выполнения всех итераций выводит список из фамилий студентов

3 модуль (Calculating_the_Number_of_Points)
основной рассчётный модуль в котором прописана вся логика вычисления оценки 
delta_day выводит разность дней между первой и второй введёнными датами
Вычисления производятся посредством метода days переводя даты методом fromisoformat в удобный для питона вид
output_weeks выводит число недель в зависимости от введённого числа дней (выводит -1 для нахождения случая, когда студент уложился в дэдайн)
output_assessment принимая число недель выводит оценку (в случае приёма -1 выводит 5 автоматически без рассчётов)
