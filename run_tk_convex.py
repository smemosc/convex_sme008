#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon, Figure

# Решил добавить выбор цвета в аргументах (для наглядности)


def void_draw(self, tk, color='black'):
    pass


def point_draw(self, tk, color='black'):
    tk.draw_point(self.p)


def segment_draw(self, tk, color='black'):
    tk.draw_line(self.p, self.q, color)


def polygon_draw(self, tk, color='black'):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first(), color)
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)

tk = TkDrawer()
f = Void()
tk.clean()

# Задаем прямую
print("Заданная прямая")
Figure.fp1 = R2Point()
Figure.fp2 = R2Point()
print("\nТочки плоскости")

# # для удобства, рисуем прямую на основе заданных точек
# # (tkinter как я понял не поддерживает прямые, а только отрезки,
# # поэтому просто будем рисовать длинный отрезок)
# x1, y1, x2, y2 = Figure.fp1.x, Figure.fp1.y, Figure.fp2.x, Figure.fp2.y
# x3 = 10
# x4 = -10
# try:
#     y3 = (x3 - x1) * (y2 - y1) / (x2 - x1) + y1
#     y4 = (x4 - x1) * (y2 - y1) / (x2 - x1) + y1
# except (ZeroDivisionError):
#     x3 = Figure.fp1.x
#     x4 = Figure.fp1.x
#     y3 = Figure.fp1.y + 1000
#     y4 = Figure.fp1.y - 1000

try:
    # рисуем заданную "прямую"
    s = Segment(Figure.fp1, Figure.fp2)
    s.draw(tk, 'red')
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk, 'green')
        # рисуем заданную "прямую"
        s.draw(tk, 'red')
        # также выводим сумму углов
        # D - сумма углов
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print(f"D = {f.sum_of_angles()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
