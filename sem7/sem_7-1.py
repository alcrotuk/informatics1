def is_not_number(x):
    return type(x) != int and type(x) != float


class Vector:
    def __init__(self, x=0, y=0, z=0):
        if type(x) == str:
            if '{' in x:
                x, y, z = list(map(eval, x[1:-1].split(', ')))
            else:
                x, y, z = list(map(eval, x.split()))
        elif is_not_number(x) | is_not_number(y) | is_not_number(z):
            print('Argument is not a number')
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, object):
        if not is_not_number(object):
            return Vector(self.x * object, self.y * object, self.z * object)
        elif type(object) == Vector:
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __truediv__(self, number):
        return self * (1 / number)

    def ploshad(self,o1,o2):
        d = o1-self
        b = o2 -self
        x = d.y*b.z-d.z*b.y
        y = -(d.x*b.z - d.z*b.x)
        z = d.x*b.y - d.y*b.x
        s = Vector(x, y, z)
        S = abs(s)/2
        return S


n = int(input())
m = []
for i in range(n):
    m.append(Vector(input()))
answer = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            c = m[i].ploshad(m[j], m[k])
            answer = max(answer, c)
print(answer)