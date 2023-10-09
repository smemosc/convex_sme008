---
date: 
author:
- Е.А. Роганов
title: Проект «Выпуклая оболочка»
---

### Постановка задачи

Необходимо написать программу, находящую выпуклую оболочку последовательно
поступающих точек плоскости и вычисляющую её периметр и площадь. Решение
должно быть индуктивным, что означает определение выпуклой оболочки и
вычисление её характеристик сразу после поступления очередной точки с
использованием методов теории индуктивных функций.

## Задание модификации

Вычисляется сумма углов, под которыми рёбра выпуклой оболочки пересекают заданную прямую. 
Прямая задаётся двумя различными точками плоскости. Возвращаемое значение: сумма углов в градусах.

## Идея модификации

В класса `R2Point` были реализованы методы `is_cross` и `angle_deg`, которые проверяют персекаются ли заданные 
прямая и отрезок и находят угол в градусах между пересекающимися прямой и отрезком. Если общей точки у отрезка и прямой нет, то 
угол 0.

В абстрактном классе `Figure`реализован новый метод `sum_of_angles`. Естественно для `Figure`, `Void`, `Point` угол равен нулю.
В классе `Segment` этот метод определен по-другому: если прямая и отрезок, задаваемый классом `Segment` пересекаются, то возвращаем
значение этого угла.

В классе `Polygon` все менее тривиально. Одним из полей класса становится `_sum_of_angles`, который равен сумме углов между 
ребрами треугольника. Для того, чтобы программа была индуктивной, не следует пересчитывать каждый раз сумму углов между прямой и 
всеми ребрами выпуклой оболочки. Достаточно просто вычитать углы, которые были образованы прямой и удаленным ребром. Также следует
добавлять к сумме углов углы, образованные между прямой и новыми ребрами, которые добавляются при соединении новой точки с выпуклой 
оболочкой.


### Краткий комментарий к решению

- Ключевое понятие проекта: *освещённость ребра из точки* 
- Вспомогательные классы:
    - `R2Point` — точка на плоскости
    - `Deq` — контейнер дек (double ended queue)
- Основные классы:
    - `Figure` — «абстрактная» фигура
    - `Void` — нульугольник
    - `Point` — одноугольник
    - `Segment` — двуугольник
    - `Polygon` — многоугольник
- Файлы проекта:
    - `README.md` — данный файл
    - `README.html` — полученный из файла `README.md` `html`-файл
    - `r2point.py` — реализация класса `R2Point`
    - `deq.py` —  реализация класса `Deq`
    - `convex.py` — реализация основных классов
    - `run_convex.py` — файл запуска
    - `tk_drawer.py` — интерфейс к графической библиотеке
    - `run_tk_convex.py` — файл запуска с использованием графики
    - `tests/test_r2point.py` — тесты к классу `R2Point`
    - `tests/test_convex.py` — тесты к основным классам

Файлы `run_tk_convex.py` и `run_tk_convex.py` являются исполняемыми (они имеют
бит `x`), в первой строке каждого из них используется [шебанг](https://ru.wikipedia.org/wiki/%D0%A8%D0%B5%D0%B1%D0%B0%D0%BD%D0%B3_(Unix)) и команда `env` с
опцией (ключом) `-S`. Это обеспечивает передачу интерпретатору языка Python
опции (ключа) `-B`, отменяющего генерацию `pyc`-файлов в директории
`__pycache__`.

### Соблюдение соглашений о стиле программного кода

Для языка Python существуют [соглашения о стиле
кода](https://www.python.org/dev/peps/pep-0008/). Они являются лишь
рекомендациями (интерпретатор игнорирует их нарушение), но основную их
часть при написании программ целесообразно соблюдать. Существует простой
способ проверить соблюдение считающегося правильным
стиля записи кода с помощью утилиты (программы) `pycodestyle`. Утилита
`yapf` позволяет даже изменить код в соответствии с этими соглашениями.

Команда 

    pycodestyle r2point.py

позволяет, например, проверить соблюдение стиля для файла `r2point.py`.
С помощью очень мощной и часто используемой утилиты `find` проверить
корректность стиля всех файлов проекта можно так:

    find . -name '*.py' -exec pycodestyle {} \;

Эта команда находит все файлы с расширением `py` и запускает программу
`pycodestyle` последовательно для каждого из них.

### Запуск тестов

Уже известная нам команда (см. материал, посвящённый тестированию программ)

    python -B -m pytest -p no:cacheprovider tests

запускает pytest, выполняя все начинающиеся с `test` методы классов,
имена которых начинаются с `Test`, содержащиеся во всех файлах `test_*.py`
директории `tests`.

### Запуск программы

`./run_convex.py`

### Запуск программы с графическим интерфейсом

`./run_tk_convex.py`
