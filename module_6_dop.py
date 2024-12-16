import math

# Базовый класс для всех фигур
class Figure:
    def __init__(self, color=(0, 0, 0), *sides):
        # Инициализация цвета
        self.__color = None
        self.set_color(*color)

        # Проверка количества сторон
        if len(sides) != self.sides_count:
            sides = [1 for _ in range(self.sides_count)]

        self.__sides = sides
        self.filled = False

    @property
    def sides_count(self):
        return 0

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        # Проверка корректности цвета
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])

    def set_color(self, r, g, b):
        # Установка цвета, если он корректен
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, new_sides):
        # Проверка корректности сторон
        return (
                len(new_sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        # Установка сторон, если они корректны
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        # Возвращает периметр фигуры
        return sum(self.__sides)

# Класс для круга
class Circle(Figure):
    @property
    def sides_count(self):
        return 1

    @property
    def radius(self):
        # Расчет радиуса по длине окружности
        circumference = self.get_sides()[0]
        return circumference / (2 * math.pi)

    def get_square(self):
        # Расчет площади круга
        return math.pi * self.radius ** 2

# Класс для треугольника
class Triangle(Figure):
    @property
    def sides_count(self):
        return 3

    def get_square(self):
        # Расчет площади треугольника по формуле Герона
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Класс для куба
class Cube(Figure):
    @property
    def sides_count(self):
        return 12

    def __init__(self, color=(0, 0, 0), *sides):
        # Инициализация сторон куба
        if len(sides) == 1:
            sides = [sides[0]] * 12
        elif len(sides) != 12:
            sides = [1] * 12
        super().__init__(color, *sides)

    def get_volume(self):
        # Расчет объема куба
        edge_length = self.get_sides()[0]
        return edge_length ** 3

    def set_sides(self, *new_sides):
        # Установка сторон куба
        if len(new_sides) == 1:
            new_sides = [new_sides[0]] * 12
        super().set_sides(*new_sides)

# Создание объектов
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())  
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина
print(len(circle1))

# Проверка объёма (куба)
print(cube1.get_volume())
