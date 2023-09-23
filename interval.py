import matplotlib.pyplot as plt

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
        plt.bar(x, y, 0.1)
        plt.title('Гистограмма распределения')
        plt.xlabel('x')
        plt.ylabel('Частоты')
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