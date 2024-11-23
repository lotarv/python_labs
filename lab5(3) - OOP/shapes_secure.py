import math

class Shape:
    def __init__(self, id, x=0, y=0):
        if not isinstance(id, str) or not id.strip():
            raise ValueError("Идентификатор должен быть непустой строкой.")
        self.id = id
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise TypeError("Координаты dx и dy должны быть числами.")
        self.x += dx
        self.y += dy

    def area(self):
        raise NotImplementedError("Метод area() должен быть реализован в подклассе.")
    
    @staticmethod
    def compare(t1, t2):
        if not (isinstance(t1, Shape) and isinstance(t2, Shape)):
            raise TypeError("Оба аргумента должны быть объектами класса Shape.")
        area1 = t1.area()
        area2 = t2.area()
        if area1 > area2:
            return f"Объект {t1.id} больше объекта {t2.id} по площади."
        elif area1 < area2:
            return f"Объект {t1.id} меньше объекта {t2.id} по площади."
        else:
            return f"Объекты {t1.id} и {t2.id} равны по площади."

class Triangle(Shape):
    def __init__(self, id, side):
        super().__init__(id)
        if side <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом.")
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

class Pentagon(Shape):
    def __init__(self, id, side):
        super().__init__(id)
        if side <= 0:
            raise ValueError("Сторона пятиугольника должна быть положительным числом.")
        self.side = side

    def area(self):
        return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))

try:
    triangle = Triangle("Triangle1", side=5)
    pentagon = Pentagon("Pentagon1", side=4)

    print(f"Треугольник (ID={triangle.id}) с площадью: {triangle.area():.2f}")
    print(f"Пятиугольник (ID={pentagon.id}) с площадью: {pentagon.area():.2f}")

    print(Shape.compare(triangle, 123))

    triangle.move(2, 3)
    pentagon.move(-1, -1)

    print(f"Треугольник перемещен в ({triangle.x}, {triangle.y}).")
    print(f"Пятиугольник перемещен в ({pentagon.x}, {pentagon.y}).")

    triangle.move(5, 7)
    pentagon.move(-3, -8)

    print(f"Треугольник перемещен в ({triangle.x}, {triangle.y}).")
    print(f"Пятиугольник перемещен в ({pentagon.x}, {pentagon.y}).")

except ValueError as ve:
    print(f"Ошибка значения: {ve}")
except TypeError as te:
    print(f"Ошибка типа: {te}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
