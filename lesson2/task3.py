class Point:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def __add__(self, other):
        X = self.X + other.X
        Y = self.Y + other.Y
        Z = self.Z + other.Z
        return X, Y, Z

    def __sub__(self, other):
        X = self.X - other.X
        Y = self.Y - other.Y
        Z = self.Z - other.Z
        return X, Y, Z

    def __mul__(self, other):
        X = self.X * other.X
        Y = self.Y * other.Y
        Z = self.Z * other.Z
        return X, Y, Z

    def __truediv__(self, other):
        X = self.X / other.X
        Y = self.Y / other.Y
        Z = self.Z / other.Z
        return X, Y, Z

    def increase_X(self, num):
        self.X += num
        return self.X, self.Y, self.Z


point_A = Point(5, 6, 8)
point_B = Point(2, 3, 5)

print(point_A + point_B)
print(point_A - point_B)
print(point_A * point_B)
print(point_A / point_B)
print(point_A.increase_X(4))
