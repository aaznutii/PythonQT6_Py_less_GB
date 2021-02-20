""""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс
Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение
(__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек
в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все
оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.
"""


class Cell:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        result = self.count + other.count
        return result

    def __sub__(self, other):
        if self.count - other.count > 0:
            result = self.count - other.count
        else:
            result = 'Вычитание невозможно'
        return result

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return int(self.count / other.count)

    def make_order(self, series):
        series_list = [self.count // series, self.count % series]
        if series_list[0] == 0:
            return '*' * series_list[1]
        else:
            return ('*' * series + '\n') * series_list[0] + ('*' * series_list[1])


c = Cell(12)
c1 = Cell(6)
print(c + c1)
print(c - c1)
print(c * c1)
print(c / c1)
print(c.make_order(5))