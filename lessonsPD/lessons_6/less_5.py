"""
5.	Реализовать класс Stationery (канцелярская принадлежность).

●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
«Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен
выводить уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title
        self.draw()
        print(f'{self.title}')
        print("_____________")

    def draw(self):
        print('Запуск отрисовки: ')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой: ')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом: ')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером: ')


Stationery('Я чувствовал себя северной стороной лошади, идущей на Юг')
Pen('ШвабраКадабра')
Pencil("КрабаНаБобра")
Handle("Смесь бульдога с мотоциклом")
