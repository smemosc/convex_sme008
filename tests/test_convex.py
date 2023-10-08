from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Void()

    # Нульугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        assert isinstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь нульугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)

    def test_sum_of_angles(self):
        assert self.f.sum_of_angles() == 0


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0))

    # Одноугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        assert isinstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь одноугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)

    def test_sum_of_angles(self):
        assert self.f.sum_of_angles() == 0


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure.fp1 = R2Point(0, 0)
        Figure.fp2 = R2Point(1, 0)
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    # Двуугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        assert isinstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    # Площадь двуугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    # При добавлении точки двуугольник может превратиться в другой двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)

    # Проверяем сумму углов у сегмента
    def test_sum_of_angles_1(self):
        s = Segment(R2Point(0.0, 0.0), R2Point(0.0, 1.0))
        assert s.sum_of_angles() == approx(90)

    def test_sum_of_angles_2(self):
        s = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))
        assert s.sum_of_angles() == 0

    def test_sum_of_angles_3(self):
        s = Segment(R2Point(0.0, -1.0), R2Point(0.0, 0.0))
        assert s.sum_of_angles() == approx(90)

    def test_sum_of_angles_4(self):
        s = Segment(R2Point(0.0, -1.0), R2Point(0.0, 1.0))
        assert s.sum_of_angles() == approx(90)

    def test_sum_of_angles_5(self):
        s = Segment(R2Point(-1.0, -1.0), R2Point(1.0, 1.0))
        assert s.sum_of_angles() == approx(45)


class TestPolygon:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure.fp1 = R2Point(0, 0)
        Figure.fp2 = R2Point(0, 1)
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    # Многоугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon(self):
        assert isinstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        assert self.f.points.size() == 3
    #   добавление точки внутрь многоугольника не меняет их количества

    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3
    #   добавление другой точки может изменить их количество

    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4
    #   изменения выпуклой оболочки могут и уменьшать их количество

    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
                    R2Point(
                        0.8,
                        0.9)).add(
                            R2Point(
                                0.9,
                                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))
    #   добавление точки может его изменить

    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_аrea1(self):
        assert self.f.area() == approx(0.5)
    #   добавление точки может увеличить площадь

    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)

    # Проверяем сумму углов
    def test_sum_of_angles_1(self):
        f = Polygon(R2Point(0.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(0.0, 1.0))
        assert f.sum_of_angles() == approx(135)

    def test_sum_of_angles_2(self):
        f = Polygon(R2Point(-1.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(0.0, 1.0))
        assert f.sum_of_angles() == approx(180)

    def test_sum_of_angles_3(self):
        f = Polygon(R2Point(-1.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(-1.0, 2.0))
        assert f.sum_of_angles() == approx(135)

    def test_sum_of_angles_4(self):
        f = Polygon(R2Point(0.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(0.0, 1.0))
        assert f.add(R2Point(1, 1)).sum_of_angles() == approx(180)

    def test_sum_of_angles_5(self):
        f = Polygon(R2Point(-1.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(0.0, 1.0))
        assert f.add(R2Point(-1, 1)).sum_of_angles() == approx(225)

    def test_sum_of_angles_6(self):
        f = Polygon(R2Point(-1.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(0.0, 1.0))
        assert f.add(R2Point(-1, 2)).sum_of_angles() == approx(135)

    def test_sum_of_angles_7(self):
        f = Polygon(R2Point(-1.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(-1.0, 2.0))
        assert f.add(R2Point(1, 2)).sum_of_angles() == approx(180)

    def test_sum_of_angles_8(self):
        f = Polygon(R2Point(-1.0, 0.0),
                    R2Point(1.0, 0.0),
                    R2Point(-1.0, 2.0))
        assert f.add(R2Point(0, -1)).sum_of_angles() == approx(135)

        # python -B -m pytest -p no:cacheprovider tests/test_convex.py
