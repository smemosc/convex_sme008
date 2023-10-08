#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void

# Задаем точки прямой
print("Заданная прямая")
Figure.fp1 = R2Point()
Figure.fp2 = R2Point()
print("\nТочки плоскости")

f = Void()
try:
    while True:
        f = f.add(R2Point())
        # Также выводим сумму углов
        # D - сумма углов
        print(f"S = {f.area()}, P = {f.perimeter()}, D = {f.sum_of_angles()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
