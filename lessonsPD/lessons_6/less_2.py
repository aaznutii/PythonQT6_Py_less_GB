"""
2.	Реализовать класс Road (дорога).
●	определить атрибуты: length (длина), width (ширина);
●	значения атрибутов должны передаваться при создании экземпляра класса;
●	атрибуты сделать защищёнными;
●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
●	проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
import itertools
import time

# class Road:
#     __length = 0
#     __width = 0


count = 0


def running(sec):
    color = ['a', 'b', 'c']
    sec = [2, 1, 3]
    for index, el in itertools.cycle(enumerate(color)):
        print(el)
        time.sleep(sec[index])
        count += 1
        yield el


x = running(5)
next(x)
next(x)
next(x)
next(x)
