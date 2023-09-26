import matplotlib.pyplot as plt
import numpy as np

class Interval:
    def __init__(self, a, b, count):
        self.a = a
        self.b = b
        self.count_data = 0
        self.count = count
        self.intervals = self.get_array_intervals(self.a, self.b, self.count)

    # Получить список интервалов
    @staticmethod
    def get_array_intervals(a, b, count):
        length = b - a
        step = length / count
        result = []
        value = b
        while value > a:
            new_segment = Segment(value)
            result.insert(0, new_segment)
            value -= step
        return result

    # Функция распределния
    @staticmethod
    def F(x, a, b):
        if x <= a:
            return 0
        elif b >= b:
            return 1
        else:
            return (x - a) / (b - a)

    # Функция плотности распределния
    @staticmethod
    def f(x, a, b):
        if a < x < b:
            return 1 / (b - a)
        else:
            return 0

    # Обратная функция распределения
    @staticmethod
    def F_reverse(gamma, a, b):
        return gamma * (b - a) + a

    def set_intervals(self, arr_arguments):
        self.clear_intervals()
        self.count_data = 0
        for value in arr_arguments:
            for element in self.intervals:
                if value <= element.argement:
                    element.increment()
                    self.count_data += 1
                    break

    def clear_intervals(self):
        for element in self.intervals:
            element.count = 0

    def __str__(self):
        strs = []
        for element in self.intervals:
            strs.append(str(element))

        return '\n'.join(strs)

    def print_gistoram(self):
        x = []
        y = []
        count_elements = self.count_data
        for element in self.intervals:
            x.append(element.argement)
            y.append(element.count / count_elements)

        # x_f = np.arange(0., 10., 0.2)
        # y_f = [self.f(elem, self.a, self.b) for elem in x_f]
        # plt.figure(figsize=(12, 6))
        # plt.subplot(131)
        plt.title('Гистограмма относительных частот')
        plt.bar(x, y, 0.1)
        # plt.subplot(133)
        # plt.plot(x_f, y_f, "go")
        # plt.suptitle('Розыгрыш стандартных непрерывных случайных величин')
        plt.show()

    def print_f_graph(self):
        plt.title('Плотность распределения')
        x = np.arange(0., 10., 0.05)
        y = [self.f(elem, self.a, self.b) for elem in x]
        plt.plot(x, y, "bo")
        # plt.xlabel('x')
        # plt.ylabel('y')
        plt.show()



class Segment:
    def __init__(self, argement):
        self.argement = argement
        self.count = 0

    def __str__(self):
        return f"{self.argement} : {self.count}"

    @property
    def argement(self):
        return self.__argement

    @argement.setter
    def argement(self, argement):
        self.__argement = argement

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def increment(self):
        self.count += 1