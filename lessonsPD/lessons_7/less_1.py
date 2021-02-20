"""
1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22      3	5	32      3	5	8	3
37	43      2	4	6       8	3	7	1
51	86      -1	64	-8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    lists = []

    def __init__(self, lists):
        self.lists = lists

    # Просто создаем цикл для обработки двух массивов по индексу, создаем экземпляр класса.
    def __add__(self, other):
        result = []
        for i in range(len(self.lists)):
            sum_x = []
            for i_el in range(len(self.lists[i])):
                x = self.lists[i][i_el] + other.lists[i][i_el]
                sum_x.append(x)
            result.append(sum_x)
        return Matrix(result)

    def __str__(self):
        strings = ''
        for list_x in self.lists:
            string = ''
            for el in list_x:
                string += f' {el} '
            strings += string + '\n'
        return strings


m = Matrix([[31, 22], [37, 43], [51, 86]])
print(m)
m1 = Matrix([[1, 1], [1, 1], [1, 1]])
print(m + m1)
m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(m2)
m3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1], [-1, 64, -8, 100]])
print(m3)