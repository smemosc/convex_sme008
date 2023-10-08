from deq import Deq
from r2point import R2Point


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    # будем считать,
    # что нульугольник и одноугольник не пересекают никакую прямую
    def sum_of_angles(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    # Считаем сумму углов между прямой и двуугольником,
    # (если не пересекаются, то 0)
    def sum_of_angles(self):
        # умножаем на 2, т.к. по условию и по логике
        # двуугольник - это два ребра, а значит пересечений либо 0, либо 2
        return R2Point.angle_deg(self.fp1, self.fp2, self.p, self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        # Сумма улов между пересекающимися ребрами с заданной прямой
        self._sum_of_angles = (R2Point.angle_deg(self.fp1, self.fp2, a, b) +
                               R2Point.angle_deg(self.fp1, self.fp2, c, b) +
                               R2Point.angle_deg(self.fp1, self.fp2, a, c))

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # Возвращаем сумму углов пересек. ребер с прямой в градусах
    def sum_of_angles(self):
        return self._sum_of_angles

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))
            # также учитывем сумму градусов
            self._sum_of_angles -= R2Point.angle_deg(
                self.fp1, self.fp2, self.points.first(), self.points.last())

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                # также учитывем сумму градусов
                self._sum_of_angles -= R2Point.angle_deg(
                    self.fp1, self.fp2, self.points.first(), p)
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                # также учитывем сумму градусов
                self._sum_of_angles -= R2Point.angle_deg(self.fp1, self.fp2,
                                                         self.points.last(), p)
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            # также учитывем сумму градусов
            self._sum_of_angles += R2Point.angle_deg(self.fp1, self.fp2,
                                                     self.points.first(), t)
            self._sum_of_angles += R2Point.angle_deg(self.fp1, self.fp2,
                                                     self.points.last(), t)

            self.points.push_first(t)

        return self


if __name__ == "__main__":
    # f = Void()
    # print(type(f), f.__dict__)
    # f = f.add(R2Point(0.0, 0.0))
    # print(type(f), f.__dict__)
    # f = f.add(R2Point(1.0, 0.0))
    # print(type(f), f.__dict__)
    # f = f.add(R2Point(0.0, 1.0))
    # print(type(f), f.__dict__)

    Figure.fp1 = R2Point(0, 0)
    Figure.fp2 = R2Point(1, 1)
    f = Polygon(
        R2Point(
            0.0, 0.0), R2Point(
            1.0, 0.0), R2Point(
            0.0, 1.0))
    print(f.sum_of_angles())
