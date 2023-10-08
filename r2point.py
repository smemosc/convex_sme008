from math import sqrt, degrees, acos


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки

    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Проверяет, пересекаются ли прямая и отрезок
    @staticmethod
    def is_cross(a, b, c, d):
        return not R2Point.area(c, a, b) or not R2Point.area(d, a, b) \
            or c.is_light(a, b) != d.is_light(a, b)

    # Угол между прямой и отрезком в градусах (если не пересекаются, то 0)
    @staticmethod
    def angle_deg(a, b, c, d):
        dot = (a.x - b.x) * (c.x - d.x) + (a.y - b.y) * (c.y - d.y)

        if R2Point.area(a, b, c) == R2Point.area(a, b, d) == 0:
            return 0
        if R2Point.is_cross(a, b, c, d):
            return degrees(acos(abs(dot) / (a.dist(b) * c.dist(d))))
        return 0.0

    # Совпадает ли точка с другой?

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    # print(type(x), x.__dict__)
    # print(x.dist(R2Point(1.0, 0.0)))
    a = R2Point(0, 0)
    b = R2Point(1, 1)
    c = R2Point(0, 0)
    d = R2Point(1, 1)
    print(R2Point.is_cross(a, b, c, d))
    print(R2Point.angle_deg(a, b, c, d))
    # print(acos(0.707))
