class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
        if isinstance(d, list):
            self.coords = d[:]

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)

    def __sub__(self, u):
        if len(self) != len(u):
            raise ValueError("dimensions must agree")
        return Vector([self.coords[i] - u.coords[i] for i in range(len(u))])

    def __neg__(self):
        return Vector([-self.coords[i] for i in range(len(self))])

    def __mul__(self, n):
        if isinstance(n, int):
            return Vector([self.coords[i] * n for i in range(len(self))])
        elif len(self) != len(n):
            raise ValueError("dimensions must agree")
        else:
            return sum([self.coords[i] * n.coords[i] for i in range(len(n))])

    def __rmul__(self, n):
        return Vector([n * self.coords[i] for i in range(len(self))])












