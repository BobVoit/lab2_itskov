import math
import random
from interval import Interval

# Функция плотности распределния
def f(x, a, b):
    if x <= a:
        return 0
    elif b >= b:
        return 1
    else:
        return (x - a) / (b - a)

# Функция распределения
def F(x, a, b):
    if a < x < b:
        return x / (b - a)
    else:
        return 0

# Обратная функция распределения
def F_reverse(gamma, a, b):
    return gamma * (b - a) + a

def main():
    
    n = 200
    N = int(math.log(n))
    a = 4
    b = 5

    data = []
    for _ in range(n):
        gamma = random.random()
        x = F_reverse(gamma, a, b)
        data.append(x)

    interval = Interval(a, b, N)

    interval.set_intervals(data)

    print(interval)

    interval.print_gistoram()

main()