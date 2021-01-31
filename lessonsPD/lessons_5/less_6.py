"""
6.	Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re
# Использовал регулярное выражение


def get_dict():
    """
    Создание словаря с исходными данными и суммой часов
    :return: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
    """
    with open('for_less_6.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    disciplines = {}
    for line in lines:
        try:
            name, subjects = line.strip('\n').split(':')
            subjects = re.findall(r'\d+', subjects)
            subjects = sum(int(el) for el in subjects)
            disciplines.update({name: subjects})
        except ValueError:
            continue
    print(disciplines)


get_dict()
