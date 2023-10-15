from pytest import approx
from math import sqrt
from r2point import R2Point


class TestR2Point:

    # Расстояние от точки до самой себя равно нулю
    def test_dist1(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(1.0, 1.0)) == approx(0.0)

    # Расстояние между двумя различными точками положительно
    def test_dist2(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(1.0, 0.0)) == approx(1.0)

    def test_dist3(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(0.0, 0.0)) == approx(sqrt(2.0))

    # Площадь треугольника равна нулю, если все вершины совпадают
    def test_area1(self):
        a = R2Point(1.0, 1.0)
        assert R2Point.area(a, a, a) == approx(0.0)

    # Площадь треугольника равна нулю, если все вершины лежат на одной прямой
    def test_area2(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 1.0), R2Point(2.0, 2.0)
        assert R2Point.area(a, b, c) == approx(0.0)

    # Площадь треугольника положительна при обходе вершин против часовой
    # стрелки
    def test_area3(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        assert R2Point.area(a, b, c) > 0.0

    # Площадь треугольника отрицательна при обходе вершин по часовой стрелке
    def test_area4(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        assert R2Point.area(a, c, b) < 0.0

    # Точки могут лежать внутри и вне "стандартного" прямоугольника с
    # противопложными вершинами (0,0) и (2,1)
    def test_is_inside1(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 0.5).is_inside(a, b) is True

    def test_is_inside2(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 0.5).is_inside(b, a) is True

    def test_is_inside3(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 1.5).is_inside(a, b) is False

    # Ребро [(0,0), (1,0)] может быть освещено или нет из определённой точки
    def test_is_light1(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, 0.0).is_light(a, b) is False

    def test_is_light2(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(2.0, 0.0).is_light(a, b) is True

    def test_is_light3(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, 0.5).is_light(a, b) is False

    def test_is_light4(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, -0.5).is_light(a, b) is True

    #
    def test_angle_deg_1(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 0)
        d = R2Point(1, 0)
        assert R2Point.angle_deg(a, b, c, d) == 0

    def test_angle_deg_2(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 1)
        d = R2Point(0, -1)
        assert R2Point.angle_deg(a, b, c, d) == 90

    def test_angle_deg_3(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(-1, -1)
        d = R2Point(1, 1)
        assert R2Point.angle_deg(a, b, c, d) == approx(45)

    def test_angle_deg_4(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 1)
        d = R2Point(1, 1)
        assert R2Point.angle_deg(a, b, c, d) == 0

    def test_angle_deg_5(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 1)
        d = R2Point(1, 2)
        assert R2Point.angle_deg(a, b, c, d) == 0

    def test_angle_deg_6(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(1, 0)
        d = R2Point(1, 1)
        assert R2Point.angle_deg(a, b, c, d) == 90

    def test_angle_deg_7(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(1, 0)
        d = R2Point(1, -1)
        assert R2Point.angle_deg(a, b, c, d) == 90

    def test_angle_deg_8(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(1, 0)
        d = R2Point(2, 2)
        assert R2Point.angle_deg(a, b, c, d) == approx(63.43494882292201)

    def test_angle_deg_9(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(4, 0)
        d = R2Point(1, 0)
        assert R2Point.angle_deg(a, b, c, d) == 0

    #
    def test_is_cross_1(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 0)
        d = R2Point(1, 0)
        assert R2Point.is_cross(a, b, c, d) == 1

    def test_is_cross_2(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 1)
        d = R2Point(0, -1)
        assert R2Point.is_cross(a, b, c, d) == 1

    def test_is_cross_3(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(-1, -1)
        d = R2Point(1, 1)
        assert R2Point.is_cross(a, b, c, d) == 1

    def test_is_cross_4(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 1)
        d = R2Point(1, 1)
        assert R2Point.is_cross(a, b, c, d) == 0

    def test_is_cross_5(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(0, 1)
        d = R2Point(1, 2)
        assert R2Point.is_cross(a, b, c, d) == 0

    def test_is_cross_6(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(1, 0)
        d = R2Point(1, 1)
        assert R2Point.is_cross(a, b, c, d) == 1

    def test_is_cross_7(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(1, 0)
        d = R2Point(1, -1)
        assert R2Point.is_cross(a, b, c, d) == 1

    def test_is_cross_8(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(1, 0)
        d = R2Point(2, 2)
        assert R2Point.is_cross(a, b, c, d) == 1

    def test_is_cross_9(self):
        a = R2Point(0, 0)
        b = R2Point(1, 0)
        c = R2Point(4, 0)
        d = R2Point(1, 0)
        assert R2Point.is_cross(a, b, c, d) == 1


# python -B -m pytest -p no:cacheprovider tests/test_r2point.py
