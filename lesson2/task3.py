class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Point(x, y, z)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Point(x, y, z)

    def increase_x(self, num):
        self.x += num
        return Point(self.x, self.y, self.z)


point_a = Point(3, 5, 2)
point_b = Point(4, 2, 1)
point_c = Point(2, 4, 5)

result1 = point_a + point_b + point_c
result2 = point_a - point_b - point_c
result3 = point_a * point_b * point_c
result4 = point_a / point_b
print(result1.x, result1.y, result1.z)
print(result2.x, result2.y, result2.z)
print(result3.x, result3.y, result3.z)
print(result4.x, result4.y, result4.z)

result = point_a.increase_x(2)
print(result.x, result.y, result.z)
