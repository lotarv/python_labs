import math

class Shape:
    def __init__(self, id, x=0, y=0):
        self.id = id
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        raise NotImplementedError("Метод area() должен быть реализован в подклассе.")
    
    def compare(t1, t2):
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
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

class Pentagon(Shape):
    def __init__(self, id, side):
        super().__init__(id)
        self.side = side

    def area(self):
        return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))


triangle = Triangle("Triangle1", side=5)
pentagon = Pentagon("Pentagon1", side=4)

print(f"Треугольник (ID={triangle.id}) с площадью: {triangle.area():.2f}")
print(f"Пятиугольник (ID={pentagon.id}) с площадью: {pentagon.area():.2f}")

print(Shape.compare(triangle, pentagon))

triangle.move(2, 3)
pentagon.move(-1, -1)

print(f"Треугольник перемещен в ({triangle.x}, {triangle.y}).")
print(f"Пятиугольник перемещен в ({pentagon.x}, {pentagon.y}).")

triangle.move(5, 7)
pentagon.move(-3, -8)

print(f"Треугольник перемещен в ({triangle.x}, {triangle.y}).")
print(f"Пятиугольник перемещен в ({pentagon.x}, {pentagon.y}).")

